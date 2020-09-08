import pyaudio
import threading
import logging

from google.cloud import speech
from google.cloud.speech import types
from google.api_core.exceptions import GoogleAPIError

from typing import Generator, Any, List
from .bases import AbstractStream, PyAudioStream
from .consts import DEFAULT_ENCODING_STT, DEFAULT_RATE

__all__ = ['RecordingStream', 'SpeechToTextStream']
logger = logging.getLogger(__name__)


class RecordingStream(PyAudioStream):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Thread-safe buffer
        self._buffer = []
        self._mutex = threading.Lock()
        self._has_data = threading.Event()

    def default_device(self) -> str:
        return self._pa.get_default_input_device_info()['name']

    def available_devices(self) -> List[dict]:
        return [device for device in self._all_devices()
                if device['maxInputChannels'] > 0 and
                device['defaultSampleRate'] == self.sample_rate]

    @property
    def stream(self) -> Generator[bytes, Any, None]:
        return super().stream

    def _write_buffer(self, in_data, frame_count, time_info, status_flags):
        with self._mutex:
            self._buffer.append(in_data)
            self._has_data.set()
        return None, pyaudio.paContinue

    def _start_stream(self) -> Generator[bytes, Any, None]:
        if self._pa_stream is None:
            self.open()
        while self.is_open:
            self._has_data.wait()
            with self._mutex:
                data = self._buffer
                self._buffer = []
                self._has_data.clear()
            yield b''.join(data)

    def _open_pa_stream(self):
        self._pa_stream = self._pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.rate,
            input=True,
            input_device_index=self._device_idx,
            frames_per_buffer=self.chunk,
            stream_callback=self._write_buffer
        )


class SpeechToTextStream(AbstractStream):
    def __init__(self, device: str = None, encoding: int = DEFAULT_ENCODING_STT,
                 rate: int = DEFAULT_RATE, interim_results=False,
                 language_code='en-US', punctuation: bool = True,
                 *args, **kwargs):
        self._input_stream = RecordingStream(device=device, *args, **kwargs)
        self._client = speech.SpeechClient()

        recognition_config = types.RecognitionConfig(
            encoding=encoding,
            sample_rate_hertz=rate,
            language_code=language_code,
            enable_automatic_punctuation=punctuation
        )
        stream_config = types.StreamingRecognitionConfig(
            config=recognition_config,
            interim_results=interim_results
        )

        self._config = stream_config

    @property
    def stream(self) -> Generator[str, Any, None]:
        return super().stream

    def _start_stream(self) -> Generator[str, Any, None]:
        requests = (types.StreamingRecognizeRequest(audio_content=data)
                    for data in self._input_stream)
        stream = self._client.streaming_recognize(self._config, requests)

        for response in stream:
            try:
                result = response.results[0]
                best = result.alternatives[0]
                yield best.transcript
            except IndexError:
                pass
            except GoogleAPIError as e:
                logger.error(e)


def main():
    AIRPODS = 'Headset (Daniel’s AirPods Hands-Free AG Audio)'
    with SpeechToTextStream(device=AIRPODS) as stream:
        for transcript in stream:
            print(transcript)


if __name__ == '__main__':
    main()
