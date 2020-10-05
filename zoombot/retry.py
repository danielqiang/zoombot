import logging
from functools import wraps


def on_exception(
    exc, max_retries: int = 10, logger: logging.Logger = None
):
    def _on_exception(method):
        @wraps(method)
        def wrapped(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return method(*args, **kwargs)
                except exc as e:
                    if logger:
                        logger.error(e)
            return method(*args, **kwargs)

        return wrapped

    return _on_exception
