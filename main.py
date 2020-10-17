from zoombot.streams import SpeechToTextStream, TextToSpeechStream
from zoombot.mitsuku import Mitsuku
from zoombot.consts import Voices

from contextlib import ExitStack

VOICE = Voices.DEFAULT
USERNAME = "Daniel"
BOTNAME = "ZoomBot"


def _format_message(user: str, message: str):
    from textwrap import fill

    # Remove non-breaking space; assumes `message`
    # only has extended ascii characters
    # (decimal ascii code < 256)
    message = message.replace(chr(160), "")

    # Wrap lines, dropping all whitespace except newlines
    indent = " " * (len(user) + 2)
    lines = []
    for i, line in enumerate(message.split("\n")):
        if i == 0:
            filled = fill(line, subsequent_indent=indent)
        else:
            filled = fill(
                line, initial_indent=indent, subsequent_indent=indent
            )
        lines.append(filled)

    formatted = "\n".join(lines)
    return f"{user}: {formatted}"


def talk():
    with ExitStack() as stack:
        stt_stream = stack.enter_context(SpeechToTextStream())
        tts_stream = stack.enter_context(
            TextToSpeechStream(
                language_code=VOICE.language_code,
                voice_name=VOICE.name,
            )
        )
        mitsuku = stack.enter_context(Mitsuku())

        print("ZoomBot initialized. Ready to go!")
        print("=" * 40)

        for message in stt_stream:
            print(_format_message(USERNAME, message))
            response = mitsuku.send(message)
            print(_format_message(BOTNAME, response))
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

            # Process voice command here
            # make API call to spotify/youtube, get response
            print(_format_message(USERNAME, message))
            response = mitsuku.send(message)
            prev_response = response
            print(_format_message(BOTNAME, response))
            tts_stream.write(response)


def main():
    talk()
    # zoom()


if __name__ == "__main__":
    main()
