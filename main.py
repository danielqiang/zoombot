from zoombot.speech_to_text import SpeechToTextStream
from zoombot.text_to_speech import TextToSpeechStream
from zoombot.mitsuku import Mitsuku

from contextlib import ExitStack
from textwrap import fill


def main():
    with ExitStack() as stack:
        stt_stream = stack.enter_context(SpeechToTextStream())
        tts_stream = stack.enter_context(TextToSpeechStream())
        mitsuku = stack.enter_context(Mitsuku())

        print('ZoomBot initialized. Ready to go!')
        print('=' * 40)

        for message in stt_stream:
            print(f'Daniel: {fill(message, subsequent_indent=" " * 8)}')
            response = mitsuku.send(message)
            print(f'ZoomBot: {fill(response, subsequent_indent=" " * 9)}')
            tts_stream.write(response)


if __name__ == '__main__':
    main()
