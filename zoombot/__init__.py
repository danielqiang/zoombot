from .bases import AbstractStream, PyAudioStream
from .speech_to_text import RecordingStream, SpeechToTextStream
from .text_to_speech import OutputStream, TextToSpeechStream
from .mitsuku import Mitsuku
from .consts import *
from .enums import Voices

import logging

# Log all messages as white text
WHITE = "\033[1m"
logging.basicConfig(level=logging.INFO,
                    format=WHITE + "%(asctime)s.%(msecs)03d [%(name)s] "
                                   "%(levelname)s: %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S')
