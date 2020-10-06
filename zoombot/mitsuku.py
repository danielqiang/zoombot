import logging
import requests

from json import JSONDecodeError
from requests import RequestException
from zoombot import retry

__all__ = ["Mitsuku"]
logger = logging.getLogger(__name__)


class Mitsuku:
    """Unofficial API wrapper for Mitsuku chatbot
    on Pandorabots."""

    _BOTKEY = (
        "n0M6dW2XZacnOgCWTp0FRYUuMjSfCkJGgobNpg"
        "Pv9060_72eKnu3Yl-o1v2nFGtSXqfwJBG2Ros~"
    )
    _ENDPOINT = "https://miapi.pandorabots.com/talk"

    def __init__(self, client_name: str = None):
        self.client_name = client_name or self._gen_client_name()
        self.session = requests.Session()
        # Initial message to obtain session id
        self.session_id = self._send("xintro")["sessionid"]

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.session.close()

    @staticmethod
    def _to_extended_ascii(s: str):
        return "".join(c for c in s if ord(c) < 256)

    @staticmethod
    def _gen_client_name():
        import time

        ms = int(time.time() * 1000)
        name = f"kukilp-{ms:x}"
        return name

    @retry.on_exception(
        (RequestException, JSONDecodeError),
        max_retries=3,
        logger=logger,
    )
    def _send(self, message: str, session_id: int = None) -> dict:
        form_data = {
            "input": message,
            "session_id": session_id,
            "channel": 6,
            "botkey": self._BOTKEY,
            "client_name": self.client_name,
        }
        headers = {"Referer": "https://www.pandorabots.com/mitsuku/"}
        resp = self.session.post(
            self._ENDPOINT, headers=headers, data=form_data
        )
        return resp.json()

    def send(
        self,
        message: str,
        remove_images: bool = True,
        force_ascii_response: bool = True,
    ) -> str:
        resp_data = self._send(message, self.session_id)
        response = resp_data["responses"][0]

        if remove_images:
            import re

            pattern = re.compile(r"<image>.*?</image>")
            response = pattern.sub("", response)

        if force_ascii_response:
            response = self._to_extended_ascii(response)
        return response


def main():
    with Mitsuku() as mitsuku:
        resp = mitsuku.send(
            "What is the weather like today in Seattle?"
        )
        print(resp)


if __name__ == "__main__":
    main()
