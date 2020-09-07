import pyaudio

from abc import ABC, abstractmethod
from typing import Generator, List, Any
from .consts import DEFAULT_RATE, DEFAULT_CHUNK, DEFAULT_SAMPLE_RATE

__all__ = ['AbstractStream', 'PyAudioStream']


class AbstractStream(ABC):
    # stream singleton
    _stream: Generator[Any, Any, None] = None

    @abstractmethod
    def _start_stream(self) -> Generator[Any, Any, None]:
        raise NotImplementedError

    @property
    def stream(self) -> Generator[Any, Any, None]:
        if self._stream is None:
            self._stream = self._start_stream()
        return self._stream

    def open(self):
        pass

    def close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.stream)


class PyAudioStream(AbstractStream):
    def __init__(self, rate: int = DEFAULT_RATE, chunk: int = DEFAULT_CHUNK,
                 sample_rate: int = DEFAULT_SAMPLE_RATE, device: str = None):
        self.rate = rate
        self.chunk = chunk
        self.sample_rate = sample_rate

        self._pa = pyaudio.PyAudio()
        self._pa_stream = None  # pyaudio.Stream object, initialized in open()

        self.is_open = False

        devices = {device['name']: device
                   for device in self.available_devices()}
        if (device is not None) and device not in devices:
            raise ValueError(f'Could not find device: {device}')
        self.device = device or self.default_device()
        self.device_info = devices[self.device]
        self._device_idx = devices[self.device]['index']

    @abstractmethod
    def default_device(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def available_devices(self) -> List[dict]:
        raise NotImplementedError

    @abstractmethod
    def _open_pa_stream(self):
        # Must initialize self._pa_stream
        raise NotImplementedError

    def _all_devices(self) -> Generator[dict, Any, None]:
        for i in range(self._pa.get_device_count()):
            yield self._pa.get_device_info_by_index(i)

    def all_devices(self) -> List[dict]:
        return list(self._all_devices())

    def open(self) -> "PyAudioStream":
        self._open_pa_stream()
        self.is_open = True
        return self

    def close(self):
        self._pa_stream.stop_stream()
        self._pa_stream.close()
        self.is_open = False

        self._pa.terminate()
