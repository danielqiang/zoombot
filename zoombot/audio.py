import pyaudio
import threading

from abc import abstractmethod
from typing import Generator, List
from .consts import DEFAULT_RATE, DEFAULT_CHUNK, DEFAULT_SAMPLE_RATE
from .bases import AbstractStream

__all__ = ["PyAudioStream", "RecordingStream", "PlaybackStream"]


class PyAudioStream(AbstractStream):
    def __init__(
        self,
        rate: int = DEFAULT_RATE,
        chunk: int = DEFAULT_CHUNK,
        sample_rate: int = DEFAULT_SAMPLE_RATE,
        device: str = None,
    ):
        self.rate = rate
        self.chunk = chunk
        self.sample_rate = sample_rate

        self._pa = pyaudio.PyAudio()
        # pyaudio.Stream object, initialized in _open_pa_stream()
        self._pa_stream = None

        self.is_open = False

        devices = {device["name"]: device
                   for device in self.available_devices()}
        if (device is not None) and device not in devices:
            raise ValueError(f"Could not find device: {device}")
        self.device = device or self.default_device()
        self.device_info = devices[self.device]
        self._device_idx = devices[self.device]["index"]

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

    def _all_devices(self) -> Generator[dict, None, None]:
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


class RecordingStream(PyAudioStream):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Thread-safe buffer
        self._buffer = []
        self._mutex = threading.Lock()
        self._has_data = threading.Event()

    def default_device(self) -> str:
        return self._pa.get_default_input_device_info()["name"]

    def available_devices(self) -> List[dict]:
        return [
            device
            for device in self._all_devices()
            if device["maxInputChannels"] > 0
            and device["defaultSampleRate"] == self.sample_rate
        ]

    @property
    def stream(self) -> Generator[bytes, None, None]:
        return super().stream

    def _write_buffer(self, in_data, frame_count, time_info, status_flags):
        with self._mutex:
            self._buffer.append(in_data)
            self._has_data.set()
        return None, pyaudio.paContinue

    def _start_stream(self) -> Generator[bytes, None, None]:
        if self._pa_stream is None:
            self.open()
        while self.is_open:
            self._has_data.wait()
            with self._mutex:
                data = self._buffer
                self._buffer = []
                self._has_data.clear()
            yield b"".join(data)

    def _open_pa_stream(self):
        self._pa_stream = self._pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.rate,
            input=True,
            input_device_index=self._device_idx,
            frames_per_buffer=self.chunk,
            stream_callback=self._write_buffer,
        )


class PlaybackStream(PyAudioStream):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.stream.send(None)

    def default_device(self) -> str:
        return self._pa.get_default_output_device_info()["name"]

    def available_devices(self) -> List[dict]:
        return [
            device
            for device in self._all_devices()
            if device["maxOutputChannels"] > 0
            and device["defaultSampleRate"] == self.sample_rate
        ]

    @property
    def stream(self) -> Generator[None, bytes, None]:
        return super().stream

    def _start_stream(self) -> Generator[None, bytes, None]:
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
            frames_per_buffer=self.chunk,
        )

    def write(self, data: bytes):
        self.stream.send(data)
