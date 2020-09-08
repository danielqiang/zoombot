from zoombot.speech_to_text import SpeechToTextStream
from zoombot.text_to_speech import TextToSpeechStream
from zoombot.mitsuku import Mitsuku
from zoombot.consts import Voices

from contextlib import ExitStack
from textwrap import fill


def sequence_diff(s1: str, s2: str):
    from difflib import SequenceMatcher
    from string import punctuation

    # remove punctuation, casing and leading/trailing whitespace
    trans_table = str.maketrans('', '', punctuation)
    s1 = s1.lower().strip().translate(trans_table)
    s2 = s2.lower().strip().translate(trans_table)

    similarity = SequenceMatcher(None, s1, s2).ratio()
    return similarity


def main():
    with ExitStack() as stack:
        # Female WaveNet, en-US
        voice = Voices.WaveNet.EN_US_WAVENET_H

        vb_cable_input = 'CABLE Input (VB-Audio Virtual C'
        vb_cable_output = 'CABLE Output (VB-Audio Virtual '

        stt_stream = stack.enter_context(
            SpeechToTextStream(
                device=vb_cable_output
            )
        )
        tts_stream = stack.enter_context(
            TextToSpeechStream(
                device=vb_cable_input,
                language_code=voice.language_code,
                voice_name=voice.name
            )
        )
        mitsuku = stack.enter_context(Mitsuku())

        print('ZoomBot initialized. Ready to go!')
        print('=' * 40)

        prev_response = ''
        for message in stt_stream:
            # ZoomBot currently echos when using VB Cable. If the message
            # is too similar to the previous response, assume it is an echo
            # and skip it.
            if sequence_diff(prev_response, message) > 0.85:
                continue
            print(f'Daniel: {fill(message, subsequent_indent=" " * 8)}')
            response = mitsuku.send(message)
            prev_response = response
            print(f'ZoomBot: {fill(response, subsequent_indent=" " * 9)}')
            tts_stream.write(response)


if __name__ == '__main__':
    main()
