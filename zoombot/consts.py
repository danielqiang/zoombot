from google.cloud import texttospeech as tts
from google.cloud.speech import enums

DEFAULT_RATE = 24000
DEFAULT_CHUNK = DEFAULT_RATE // 10  # 100ms
DEFAULT_SAMPLE_RATE = 44100
DEFAULT_ENCODING_STT = enums.RecognitionConfig.AudioEncoding.LINEAR16
DEFAULT_ENCODING_TTS = tts.AudioEncoding.LINEAR16
