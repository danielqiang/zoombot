from zoombot.speech_to_text import SpeechToTextStream
from zoombot.text_to_speech import TextToSpeechStream
from zoombot.mitsuku import Mitsuku
from zoombot.consts import Voices

from contextlib import ExitStack
from textwrap import fill


def main():
    with ExitStack() as stack:
        # Female WaveNet, en-US
        voice = Voices.WaveNet.EN_US_WAVENET_H

        stt_stream = stack.enter_context(SpeechToTextStream())
        tts_stream = stack.enter_context(
            TextToSpeechStream(
                language_code=voice.language_code,
                voice_name=voice.name
            )
        )
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
