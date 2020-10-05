from .bases import AbstractStream
from .audio import PyAudioStream, RecordingStream, PlaybackStream
from .streams import SpeechToTextStream, TextToSpeechStream
from .mitsuku import Mitsuku
from .consts import *

import logging

# Log all messages as white text
WHITE = "\033[1m"
logging.basicConfig(
    level=logging.INFO,
    format=f"{WHITE}%(asctime)s.%(msecs)03d [%(name)s] "
           "%(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
