from google.cloud.speech import enums
from google.cloud import texttospeech

DEFAULT_RATE = 24000
DEFAULT_CHUNK = DEFAULT_RATE // 10  # 100ms
DEFAULT_SAMPLE_RATE = 44100
DEFAULT_ENCODING_STT = enums.RecognitionConfig.AudioEncoding.LINEAR16
DEFAULT_ENCODING_TTS = texttospeech.AudioEncoding.LINEAR16
