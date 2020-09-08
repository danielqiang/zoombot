import logging

from google.cloud import speech
from google.cloud.speech import types
from google.api_core.exceptions import GoogleAPIError

from typing import Generator, Any
from .bases import AbstractStream
from .audio import RecordingStream
from .consts import DEFAULT_ENCODING_STT, DEFAULT_RATE

__all__ = ["SpeechToTextStream"]
logger = logging.getLogger(__name__)


class SpeechToTextStream(AbstractStream):
    def __init__(
        self,
        device: str = None,
        encoding: int = DEFAULT_ENCODING_STT,
        rate: int = DEFAULT_RATE,
        interim_results=False,
        language_code="en-US",
        punctuation: bool = True,
        *args,
        **kwargs
    ):
        self._input_stream = RecordingStream(device=device, *args, **kwargs)
        self._client = speech.SpeechClient()

        recognition_config = types.RecognitionConfig(
            encoding=encoding,
            sample_rate_hertz=rate,
            language_code=language_code,
            enable_automatic_punctuation=punctuation,
        )
        stream_config = types.StreamingRecognitionConfig(
            config=recognition_config, interim_results=interim_results
        )
        self._config = stream_config

    @property
    def stream(self) -> Generator[str, Any, None]:
        return super().stream

    def _start_stream(self) -> Generator[str, Any, None]:
        requests = (
            types.StreamingRecognizeRequest(audio_content=data)
            for data in self._input_stream
        )
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
    with SpeechToTextStream() as stream:
        for transcript in stream:
            print(transcript)


if __name__ == "__main__":
    main()
