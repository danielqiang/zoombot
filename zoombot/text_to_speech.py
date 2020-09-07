import pyaudio

from google.cloud import texttospeech

from typing import Generator, List, Optional
from .bases import AbstractStream, PyAudioStream
from .consts import DEFAULT_ENCODING_TTS

__all__ = ['OutputStream', 'TextToSpeechStream']


class OutputStream(PyAudioStream):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # prime output generator
        self.stream.send(None)

    def default_device(self) -> str:
        return self._pa.get_default_output_device_info()['name']

    def available_devices(self) -> List[dict]:
        return [device for device in self._all_devices()
                if device['maxOutputChannels'] > 0]

    @property
    def stream(self) -> Generator[None, Optional[bytes], None]:
        return super().stream

    def _start_stream(self) -> Generator[None, Optional[bytes], None]:
        if self._pa_stream is None:
            self.open()
        while self.is_open:
            data = yield
            self._pa_stream.write(data)

    def _open_pa_stream(self):
        self._pa_stream = self._pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.rate,
            output=True,
            output_device_index=self._device_idx,
            frames_per_buffer=self.chunk
        )

    def write(self, data: bytes):
        self.stream.send(data)


class TextToSpeechStream(AbstractStream):
    def __init__(self, device: str = None, encoding: int = DEFAULT_ENCODING_TTS,
                 language_code: str = 'en-US', voice_name: str = 'en-AU-Wavenet-B'):
        self._output_stream = OutputStream(device=device)
        self._client = texttospeech.TextToSpeechClient()

        self._voice = texttospeech.VoiceSelectionParams(
            {'language_code': language_code,
             'name': voice_name}
        )
        self._audio_config = texttospeech.AudioConfig(
            {'audio_encoding': encoding}
        )

        self.stream.send(None)

    @property
    def stream(self) -> Generator[None, Optional[str], None]:
        return super().stream

    def _start_stream(self) -> Generator[None, Optional[str], None]:
        while True:
            message = yield
            synthesis_input = texttospeech.SynthesisInput({'text': message})
            response = self._client.synthesize_speech(
                input=synthesis_input,
                voice=self._voice,
                audio_config=self._audio_config
            )
            self._output_stream.write(response.audio_content)

    def write(self, message: str):
        self.stream.send(message)
