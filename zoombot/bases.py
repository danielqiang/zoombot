from abc import ABC, abstractmethod
from typing import Generator, Any

__all__ = [
    "AbstractStream",
    "InputStreamMixin",
    "OutputStreamMixin",
    "InputStream",
    "OutputStream",
]


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


class InputStreamMixin:
    stream: Generator[Any, None, None]

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.stream)


class OutputStreamMixin:
    stream: Generator[None, Any, None]

    def write(self, data):
        self.stream.send(data)


class InputStream(AbstractStream, InputStreamMixin):
    pass


class OutputStream(AbstractStream, OutputStreamMixin):
    pass
