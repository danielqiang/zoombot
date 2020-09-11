from zoombot.streams import SpeechToTextStream, TextToSpeechStream
from zoombot.mitsuku import Mitsuku
from zoombot.consts import Voices

from contextlib import ExitStack
from textwrap import fill

VOICE = Voices.WaveNet.CMN_CN_WAVENET_B


def talk():
    with ExitStack() as stack:
        stt_stream = stack.enter_context(SpeechToTextStream())
        tts_stream = stack.enter_context(
            TextToSpeechStream(
                language_code=VOICE.language_code,
                voice_name=VOICE.name
            )
        )
        mitsuku = stack.enter_context(Mitsuku())

        print("ZoomBot initialized. Ready to go!")
        print("=" * 40)

        for message in stt_stream:
            print(f'Daniel: {fill(message, subsequent_indent=" " * 8)}')
            response = mitsuku.send(message)
            print(f'ZoomBot: {fill(response, subsequent_indent=" " * 9)}')
            tts_stream.write(response)


def _sequence_diff(s1: str, s2: str):
    from difflib import SequenceMatcher
    from string import punctuation

    # remove punctuation, casing and leading/trailing whitespace
    trans_table = str.maketrans("", "", punctuation)
    s1 = s1.translate(trans_table).lower().strip()
    s2 = s2.translate(trans_table).lower().strip()

    similarity = SequenceMatcher(a=s1, b=s2).ratio()
    return similarity


def zoom():
    with ExitStack() as stack:
        vb_cable_input = "CABLE Input (VB-Audio Virtual C"  # speaker
        vb_cable_output = "CABLE Output (VB-Audio Virtual "  # mic

        stt_stream = stack.enter_context(
            # TODO: input device should be output of speaker, not mic
            SpeechToTextStream(input_device=vb_cable_output)
        )
        tts_stream = stack.enter_context(
            TextToSpeechStream(
                output_device=vb_cable_input,
                language_code=VOICE.language_code,
                voice_name=VOICE.name,
            )
        )
        mitsuku = stack.enter_context(Mitsuku())

        print("ZoomBot initialized. Ready to go!")
        print("=" * 40)

        prev_response = ""
        for message in stt_stream:
            # ZoomBot currently echos when using VB Cable. If the message
            # is too similar to the previous response, assume it is an echo
            # and skip it.
            if _sequence_diff(prev_response, message) > 0.85:
                continue
            print(f'Daniel: {fill(message, subsequent_indent=" " * 8)}')
            response = mitsuku.send(message)
            prev_response = response
            print(f'ZoomBot: {fill(response, subsequent_indent=" " * 9)}')
            tts_stream.write(response)


def main():
    talk()
    # zoom()


if __name__ == "__main__":
    main()
