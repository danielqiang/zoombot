import logging

from google.cloud import speech
from google.cloud import texttospeech as tts
from google.cloud.speech import (
    RecognitionConfig,
    StreamingRecognitionConfig,
    StreamingRecognizeRequest,
)
from google.api_core.exceptions import GoogleAPIError

from typing import Generator
from .bases import InputStream, OutputStream
from .audio import RecordingStream, PlaybackStream
from .consts import (
    DEFAULT_ENCODING_STT,
    DEFAULT_ENCODING_TTS,
    DEFAULT_RATE,
    Voices,
)

__all__ = ["SpeechToTextStream", "TextToSpeechStream"]
logger = logging.getLogger(__name__)


class SpeechToTextStream(InputStream):
    def __init__(
        self,
        input_device: str = None,
        encoding: int = DEFAULT_ENCODING_STT,
        rate: int = DEFAULT_RATE,
        interim_results: str = False,
        language_code: str = "en-US",
        punctuation: bool = True,
        *args,
        **kwargs
    ):
        self._input_stream = RecordingStream(
            device=input_device, *args, **kwargs
        )
        self._client = speech.SpeechClient()

        recognition_config = RecognitionConfig(
            encoding=encoding,
            sample_rate_hertz=rate,
            language_code=language_code,
            enable_automatic_punctuation=punctuation,
        )
        stream_config = StreamingRecognitionConfig(
            config=recognition_config,
            interim_results=interim_results,
        )
        self._config = stream_config

    @property
    def stream(self) -> Generator[str, None, None]:
        return super().stream

    def _start_stream(self) -> Generator[str, None, None]:
        requests = (
            StreamingRecognizeRequest(audio_content=data)
            for data in self._input_stream
        )
        stream = self._client.streaming_recognize(
            self._config, requests
        )

        for response in stream:
            try:
                result = response.results[0]
                best = result.alternatives[0]
                yield best.transcript
            except IndexError:
                pass
            except GoogleAPIError as e:
                logger.error(e)


class TextToSpeechStream(OutputStream):
    def __init__(
        self,
        output_device: str = None,
        encoding: int = DEFAULT_ENCODING_TTS,
        language_code: str = Voices.DEFAULT.language_code,
        voice_name: str = Voices.DEFAULT.name,
        *args,
        **kwargs
    ):
        self._output_stream = PlaybackStream(
            device=output_device, *args, **kwargs
        )
        self._client = tts.TextToSpeechClient()

        self._voice = tts.VoiceSelectionParams(
            {"language_code": language_code, "name": voice_name}
        )
        self._audio_config = tts.AudioConfig(
            {"audio_encoding": encoding}
        )

        self.stream.send(None)

    @property
    def stream(self) -> Generator[None, str, None]:
        return super().stream

    def _start_stream(self) -> Generator[None, str, None]:
        while True:
            message = yield
            synthesis_input = tts.SynthesisInput({"text": message})
            response = self._client.synthesize_speech(
                input=synthesis_input,
                voice=self._voice,
                audio_config=self._audio_config,
            )
            self._output_stream.write(response.audio_content)


def main():
    with SpeechToTextStream() as stream:
        for transcript in stream:
            print(transcript)


if __name__ == "__main__":
    main()
