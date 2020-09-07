import requests
import bs4

__all__ = ['Mitsuku']


class Mitsuku:
    """Unofficial API for Mitsuku chatbot
    on Pandorabots."""

    _BOTKEY = ('n0M6dW2XZacnOgCWTp0FRYUuMjSfCkJGgobNpg'
               'Pv9060_72eKnu3Yl-o1v2nFGtSXqfwJBG2Ros~')
    _ENDPOINT = 'https://miapi.pandorabots.com/talk'

    def __init__(self, client_name: str = None):
        self.client_name = client_name or self._gen_client_name()
        self.session = requests.Session()
        # Initial message to obtain session id
        self.session_id = self._send('xintro')['sessionid']

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.session.close()

    @staticmethod
    def _gen_client_name():
        import time

        ms = int(time.time() * 1000)
        name = f'kukilp-{ms:x}'
        return name

    def _send(self, message: str, session_id: int = None) -> dict:
        form_data = {
            'input': message,
            'session_id': session_id,
            'channel': 6,
            'botkey': self._BOTKEY,
            'client_name': self.client_name
        }
        headers = {'Referer': 'https://www.pandorabots.com/mitsuku/'}
        resp = self.session.post(self._ENDPOINT, headers=headers, data=form_data)
        return resp.json()

    def send(self, message: str):
        response = self._send(message, self.session_id)['responses'][0]
        soup = bs4.BeautifulSoup(response, 'html.parser')

        # Extract text, ignore images
        parts = [s for s in soup.text.split()
                 if not s.startswith('http')]
        return ' '.join(parts)


def main():
    with Mitsuku() as mitsuku:
        resp = mitsuku.send("Wow thank you")
        print(resp)


if __name__ == '__main__':
    main()
