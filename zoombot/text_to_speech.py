from google.cloud import texttospeech as tts

from typing import Generator, Optional
from .bases import AbstractStream
from .audio import OutputStream
from .consts import DEFAULT_ENCODING_TTS

__all__ = ['TextToSpeechStream']


class TextToSpeechStream(AbstractStream):
    def __init__(self, device: str = None, encoding: int = DEFAULT_ENCODING_TTS,
                 language_code: str = 'en-US', voice_name: str = 'en-AU-Wavenet-B',
                 *args, **kwargs):
        self._output_stream = OutputStream(device=device, *args, **kwargs)
        self._client = tts.TextToSpeechClient()

        self._voice = tts.VoiceSelectionParams(
            {'language_code': language_code,
             'name': voice_name}
        )
        self._audio_config = tts.AudioConfig(
            {'audio_encoding': encoding}
        )

        self.stream.send(None)

    @property
    def stream(self) -> Generator[None, Optional[str], None]:
        return super().stream

    def _start_stream(self) -> Generator[None, Optional[str], None]:
        while True:
            message = yield
            synthesis_input = tts.SynthesisInput({'text': message})
            response = self._client.synthesize_speech(
                input=synthesis_input,
                voice=self._voice,
                audio_config=self._audio_config
            )
            self._output_stream.write(response.audio_content)

    def write(self, message: str):
        self.stream.send(message)
