import enum

from collections import namedtuple
from google.cloud import texttospeech as tts
from google.cloud.texttospeech import SsmlVoiceGender

__all__ = ['Voices']

Voice = namedtuple('Type', ['language_code', 'name', 'gender', 'rate'])


class Voices:
    """Enum container for Google Cloud Speech Synthesis
    voices"""

    class Standard(enum.Enum):
        AR_XA_STANDARD_A = Voice('ar-XA', 'ar-XA-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        AR_XA_STANDARD_B = Voice('ar-XA', 'ar-XA-Standard-B', SsmlVoiceGender.MALE, 24000)
        AR_XA_STANDARD_C = Voice('ar-XA', 'ar-XA-Standard-C', SsmlVoiceGender.MALE, 24000)
        AR_XA_STANDARD_D = Voice('ar-XA', 'ar-XA-Standard-D', SsmlVoiceGender.FEMALE, 24000)
        BN_IN_STANDARD_A = Voice('bn-IN', 'bn-IN-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        BN_IN_STANDARD_B = Voice('bn-IN', 'bn-IN-Standard-B', SsmlVoiceGender.MALE, 24000)
        CMN_CN_STANDARD_A = Voice('cmn-CN', 'cmn-CN-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        CMN_CN_STANDARD_B = Voice('cmn-CN', 'cmn-CN-Standard-B', SsmlVoiceGender.MALE, 24000)
        CMN_CN_STANDARD_C = Voice('cmn-CN', 'cmn-CN-Standard-C', SsmlVoiceGender.MALE, 24000)
        CMN_CN_STANDARD_D = Voice('cmn-CN', 'cmn-CN-Standard-D', SsmlVoiceGender.FEMALE, 24000)
        CMN_TW_STANDARD_A = Voice('cmn-TW', 'cmn-TW-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        CMN_TW_STANDARD_B = Voice('cmn-TW', 'cmn-TW-Standard-B', SsmlVoiceGender.MALE, 24000)
        CMN_TW_STANDARD_C = Voice('cmn-TW', 'cmn-TW-Standard-C', SsmlVoiceGender.MALE, 24000)
        CS_CZ_STANDARD_A = Voice('cs-CZ', 'cs-CZ-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        DA_DK_STANDARD_A = Voice('da-DK', 'da-DK-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        DA_DK_STANDARD_C = Voice('da-DK', 'da-DK-Standard-C', SsmlVoiceGender.MALE, 24000)
        DA_DK_STANDARD_D = Voice('da-DK', 'da-DK-Standard-D', SsmlVoiceGender.FEMALE, 24000)
        DA_DK_STANDARD_E = Voice('da-DK', 'da-DK-Standard-E', SsmlVoiceGender.FEMALE, 24000)
        DE_DE_STANDARD_A = Voice('de-DE', 'de-DE-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        DE_DE_STANDARD_B = Voice('de-DE', 'de-DE-Standard-B', SsmlVoiceGender.MALE, 24000)
        DE_DE_STANDARD_E = Voice('de-DE', 'de-DE-Standard-E', SsmlVoiceGender.MALE, 24000)
        DE_DE_STANDARD_F = Voice('de-DE', 'de-DE-Standard-F', SsmlVoiceGender.FEMALE, 24000)
        EL_GR_STANDARD_A = Voice('el-GR', 'el-GR-Standard-A', SsmlVoiceGender.FEMALE, 22050)
        EN_AU_STANDARD_A = Voice('en-AU', 'en-AU-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        EN_AU_STANDARD_B = Voice('en-AU', 'en-AU-Standard-B', SsmlVoiceGender.MALE, 24000)
        EN_AU_STANDARD_C = Voice('en-AU', 'en-AU-Standard-C', SsmlVoiceGender.FEMALE, 24000)
        EN_AU_STANDARD_D = Voice('en-AU', 'en-AU-Standard-D', SsmlVoiceGender.MALE, 24000)
        EN_GB_STANDARD_A = Voice('en-GB', 'en-GB-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        EN_GB_STANDARD_B = Voice('en-GB', 'en-GB-Standard-B', SsmlVoiceGender.MALE, 24000)
        EN_GB_STANDARD_C = Voice('en-GB', 'en-GB-Standard-C', SsmlVoiceGender.FEMALE, 24000)
        EN_GB_STANDARD_D = Voice('en-GB', 'en-GB-Standard-D', SsmlVoiceGender.MALE, 24000)
        EN_GB_STANDARD_F = Voice('en-GB', 'en-GB-Standard-F', SsmlVoiceGender.FEMALE, 24000)
        EN_IN_STANDARD_A = Voice('en-IN', 'en-IN-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        EN_IN_STANDARD_B = Voice('en-IN', 'en-IN-Standard-B', SsmlVoiceGender.MALE, 24000)
        EN_IN_STANDARD_C = Voice('en-IN', 'en-IN-Standard-C', SsmlVoiceGender.MALE, 24000)
        EN_IN_STANDARD_D = Voice('en-IN', 'en-IN-Standard-D', SsmlVoiceGender.FEMALE, 24000)
        EN_US_STANDARD_B = Voice('en-US', 'en-US-Standard-B', SsmlVoiceGender.MALE, 24000)
        EN_US_STANDARD_C = Voice('en-US', 'en-US-Standard-C', SsmlVoiceGender.FEMALE, 24000)
        EN_US_STANDARD_D = Voice('en-US', 'en-US-Standard-D', SsmlVoiceGender.MALE, 24000)
        EN_US_STANDARD_E = Voice('en-US', 'en-US-Standard-E', SsmlVoiceGender.FEMALE, 24000)
        EN_US_STANDARD_G = Voice('en-US', 'en-US-Standard-G', SsmlVoiceGender.FEMALE, 24000)
        EN_US_STANDARD_H = Voice('en-US', 'en-US-Standard-H', SsmlVoiceGender.FEMALE, 24000)
        EN_US_STANDARD_I = Voice('en-US', 'en-US-Standard-I', SsmlVoiceGender.MALE, 24000)
        EN_US_STANDARD_J = Voice('en-US', 'en-US-Standard-J', SsmlVoiceGender.MALE, 24000)
        ES_ES_STANDARD_A = Voice('es-ES', 'es-ES-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        FIL_PH_STANDARD_A = Voice('fil-PH', 'fil-PH-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        FIL_PH_STANDARD_B = Voice('fil-PH', 'fil-PH-Standard-B', SsmlVoiceGender.FEMALE, 24000)
        FIL_PH_STANDARD_C = Voice('fil-PH', 'fil-PH-Standard-C', SsmlVoiceGender.MALE, 24000)
        FIL_PH_STANDARD_D = Voice('fil-PH', 'fil-PH-Standard-D', SsmlVoiceGender.MALE, 24000)
        FI_FI_STANDARD_A = Voice('fi-FI', 'fi-FI-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        FR_CA_STANDARD_A = Voice('fr-CA', 'fr-CA-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        FR_CA_STANDARD_B = Voice('fr-CA', 'fr-CA-Standard-B', SsmlVoiceGender.MALE, 24000)
        FR_CA_STANDARD_C = Voice('fr-CA', 'fr-CA-Standard-C', SsmlVoiceGender.FEMALE, 24000)
        FR_CA_STANDARD_D = Voice('fr-CA', 'fr-CA-Standard-D', SsmlVoiceGender.MALE, 24000)
        FR_FR_STANDARD_A = Voice('fr-FR', 'fr-FR-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        FR_FR_STANDARD_B = Voice('fr-FR', 'fr-FR-Standard-B', SsmlVoiceGender.MALE, 24000)
        FR_FR_STANDARD_C = Voice('fr-FR', 'fr-FR-Standard-C', SsmlVoiceGender.FEMALE, 24000)
        FR_FR_STANDARD_D = Voice('fr-FR', 'fr-FR-Standard-D', SsmlVoiceGender.MALE, 24000)
        FR_FR_STANDARD_E = Voice('fr-FR', 'fr-FR-Standard-E', SsmlVoiceGender.FEMALE, 24000)
        GU_IN_STANDARD_A = Voice('gu-IN', 'gu-IN-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        GU_IN_STANDARD_B = Voice('gu-IN', 'gu-IN-Standard-B', SsmlVoiceGender.MALE, 24000)
        HI_IN_STANDARD_A = Voice('hi-IN', 'hi-IN-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        HI_IN_STANDARD_B = Voice('hi-IN', 'hi-IN-Standard-B', SsmlVoiceGender.MALE, 24000)
        HI_IN_STANDARD_C = Voice('hi-IN', 'hi-IN-Standard-C', SsmlVoiceGender.MALE, 24000)
        HI_IN_STANDARD_D = Voice('hi-IN', 'hi-IN-Standard-D', SsmlVoiceGender.FEMALE, 24000)
        HU_HU_STANDARD_A = Voice('hu-HU', 'hu-HU-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        ID_ID_STANDARD_A = Voice('id-ID', 'id-ID-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        ID_ID_STANDARD_B = Voice('id-ID', 'id-ID-Standard-B', SsmlVoiceGender.MALE, 24000)
        ID_ID_STANDARD_C = Voice('id-ID', 'id-ID-Standard-C', SsmlVoiceGender.MALE, 24000)
        ID_ID_STANDARD_D = Voice('id-ID', 'id-ID-Standard-D', SsmlVoiceGender.FEMALE, 22050)
        IT_IT_STANDARD_A = Voice('it-IT', 'it-IT-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        IT_IT_STANDARD_B = Voice('it-IT', 'it-IT-Standard-B', SsmlVoiceGender.FEMALE, 24000)
        IT_IT_STANDARD_C = Voice('it-IT', 'it-IT-Standard-C', SsmlVoiceGender.MALE, 24000)
        IT_IT_STANDARD_D = Voice('it-IT', 'it-IT-Standard-D', SsmlVoiceGender.MALE, 24000)
        JA_JP_STANDARD_A = Voice('ja-JP', 'ja-JP-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        JA_JP_STANDARD_B = Voice('ja-JP', 'ja-JP-Standard-B', SsmlVoiceGender.FEMALE, 24000)
        JA_JP_STANDARD_C = Voice('ja-JP', 'ja-JP-Standard-C', SsmlVoiceGender.MALE, 24000)
        JA_JP_STANDARD_D = Voice('ja-JP', 'ja-JP-Standard-D', SsmlVoiceGender.MALE, 24000)
        KN_IN_STANDARD_A = Voice('kn-IN', 'kn-IN-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        KN_IN_STANDARD_B = Voice('kn-IN', 'kn-IN-Standard-B', SsmlVoiceGender.MALE, 24000)
        KO_KR_STANDARD_A = Voice('ko-KR', 'ko-KR-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        KO_KR_STANDARD_B = Voice('ko-KR', 'ko-KR-Standard-B', SsmlVoiceGender.FEMALE, 24000)
        KO_KR_STANDARD_C = Voice('ko-KR', 'ko-KR-Standard-C', SsmlVoiceGender.MALE, 24000)
        KO_KR_STANDARD_D = Voice('ko-KR', 'ko-KR-Standard-D', SsmlVoiceGender.MALE, 24000)
        ML_IN_STANDARD_A = Voice('ml-IN', 'ml-IN-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        ML_IN_STANDARD_B = Voice('ml-IN', 'ml-IN-Standard-B', SsmlVoiceGender.MALE, 24000)
        NB_NO_STANDARD_A = Voice('nb-NO', 'nb-NO-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        NB_NO_STANDARD_B = Voice('nb-NO', 'nb-NO-Standard-B', SsmlVoiceGender.MALE, 24000)
        NB_NO_STANDARD_C = Voice('nb-NO', 'nb-NO-Standard-C', SsmlVoiceGender.FEMALE, 24000)
        NB_NO_STANDARD_D = Voice('nb-NO', 'nb-NO-Standard-D', SsmlVoiceGender.MALE, 24000)
        NB_NO_STANDARD_E = Voice('nb-NO', 'nb-no-Standard-E', SsmlVoiceGender.FEMALE, 24000)
        NL_NL_STANDARD_A = Voice('nl-NL', 'nl-NL-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        NL_NL_STANDARD_B = Voice('nl-NL', 'nl-NL-Standard-B', SsmlVoiceGender.MALE, 24000)
        NL_NL_STANDARD_C = Voice('nl-NL', 'nl-NL-Standard-C', SsmlVoiceGender.MALE, 24000)
        NL_NL_STANDARD_D = Voice('nl-NL', 'nl-NL-Standard-D', SsmlVoiceGender.FEMALE, 24000)
        NL_NL_STANDARD_E = Voice('nl-NL', 'nl-NL-Standard-E', SsmlVoiceGender.FEMALE, 24000)
        PL_PL_STANDARD_A = Voice('pl-PL', 'pl-PL-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        PL_PL_STANDARD_B = Voice('pl-PL', 'pl-PL-Standard-B', SsmlVoiceGender.MALE, 24000)
        PL_PL_STANDARD_C = Voice('pl-PL', 'pl-PL-Standard-C', SsmlVoiceGender.MALE, 24000)
        PL_PL_STANDARD_D = Voice('pl-PL', 'pl-PL-Standard-D', SsmlVoiceGender.FEMALE, 24000)
        PL_PL_STANDARD_E = Voice('pl-PL', 'pl-PL-Standard-E', SsmlVoiceGender.FEMALE, 22050)
        PT_BR_STANDARD_A = Voice('pt-BR', 'pt-BR-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        PT_PT_STANDARD_A = Voice('pt-PT', 'pt-PT-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        PT_PT_STANDARD_B = Voice('pt-PT', 'pt-PT-Standard-B', SsmlVoiceGender.MALE, 24000)
        PT_PT_STANDARD_C = Voice('pt-PT', 'pt-PT-Standard-C', SsmlVoiceGender.MALE, 24000)
        PT_PT_STANDARD_D = Voice('pt-PT', 'pt-PT-Standard-D', SsmlVoiceGender.FEMALE, 24000)
        RU_RU_STANDARD_A = Voice('ru-RU', 'ru-RU-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        RU_RU_STANDARD_B = Voice('ru-RU', 'ru-RU-Standard-B', SsmlVoiceGender.MALE, 24000)
        RU_RU_STANDARD_C = Voice('ru-RU', 'ru-RU-Standard-C', SsmlVoiceGender.FEMALE, 24000)
        RU_RU_STANDARD_D = Voice('ru-RU', 'ru-RU-Standard-D', SsmlVoiceGender.MALE, 24000)
        RU_RU_STANDARD_E = Voice('ru-RU', 'ru-RU-Standard-E', SsmlVoiceGender.FEMALE, 24000)
        SK_SK_STANDARD_A = Voice('sk-SK', 'sk-SK-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        SV_SE_STANDARD_A = Voice('sv-SE', 'sv-SE-Standard-A', SsmlVoiceGender.FEMALE, 22050)
        TA_IN_STANDARD_A = Voice('ta-IN', 'ta-IN-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        TA_IN_STANDARD_B = Voice('ta-IN', 'ta-IN-Standard-B', SsmlVoiceGender.MALE, 24000)
        TE_IN_STANDARD_A = Voice('te-IN', 'te-IN-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        TE_IN_STANDARD_B = Voice('te-IN', 'te-IN-Standard-B', SsmlVoiceGender.MALE, 24000)
        TH_TH_STANDARD_A = Voice('th-TH', 'th-TH-Standard-A', SsmlVoiceGender.FEMALE, 22050)
        TR_TR_STANDARD_A = Voice('tr-TR', 'tr-TR-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        TR_TR_STANDARD_B = Voice('tr-TR', 'tr-TR-Standard-B', SsmlVoiceGender.MALE, 24000)
        TR_TR_STANDARD_C = Voice('tr-TR', 'tr-TR-Standard-C', SsmlVoiceGender.FEMALE, 24000)
        TR_TR_STANDARD_D = Voice('tr-TR', 'tr-TR-Standard-D', SsmlVoiceGender.FEMALE, 24000)
        TR_TR_STANDARD_E = Voice('tr-TR', 'tr-TR-Standard-E', SsmlVoiceGender.MALE, 24000)
        UK_UA_STANDARD_A = Voice('uk-UA', 'uk-UA-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        VI_VN_STANDARD_A = Voice('vi-VN', 'vi-VN-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        VI_VN_STANDARD_B = Voice('vi-VN', 'vi-VN-Standard-B', SsmlVoiceGender.MALE, 24000)
        VI_VN_STANDARD_C = Voice('vi-VN', 'vi-VN-Standard-C', SsmlVoiceGender.FEMALE, 24000)
        VI_VN_STANDARD_D = Voice('vi-VN', 'vi-VN-Standard-D', SsmlVoiceGender.MALE, 24000)
        YUE_HK_STANDARD_A = Voice('yue-HK', 'yue-HK-Standard-A', SsmlVoiceGender.FEMALE, 24000)
        YUE_HK_STANDARD_B = Voice('yue-HK', 'yue-HK-Standard-B', SsmlVoiceGender.MALE, 24000)
        YUE_HK_STANDARD_C = Voice('yue-HK', 'yue-HK-Standard-C', SsmlVoiceGender.FEMALE, 24000)
        YUE_HK_STANDARD_D = Voice('yue-HK', 'yue-HK-Standard-D', SsmlVoiceGender.MALE, 24000)

    class WaveNet(enum.Enum):
        AR_XA_WAVENET_A = Voice('ar-XA', 'ar-XA-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        AR_XA_WAVENET_B = Voice('ar-XA', 'ar-XA-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        AR_XA_WAVENET_C = Voice('ar-XA', 'ar-XA-Wavenet-C', SsmlVoiceGender.MALE, 24000)
        CMN_CN_WAVENET_A = Voice('cmn-CN', 'cmn-CN-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        CMN_CN_WAVENET_B = Voice('cmn-CN', 'cmn-CN-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        CMN_CN_WAVENET_C = Voice('cmn-CN', 'cmn-CN-Wavenet-C', SsmlVoiceGender.MALE, 24000)
        CMN_CN_WAVENET_D = Voice('cmn-CN', 'cmn-CN-Wavenet-D', SsmlVoiceGender.FEMALE, 24000)
        CMN_TW_WAVENET_A = Voice('cmn-TW', 'cmn-TW-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        CMN_TW_WAVENET_B = Voice('cmn-TW', 'cmn-TW-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        CMN_TW_WAVENET_C = Voice('cmn-TW', 'cmn-TW-Wavenet-C', SsmlVoiceGender.MALE, 24000)
        CS_CZ_WAVENET_A = Voice('cs-CZ', 'cs-CZ-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        DA_DK_WAVENET_A = Voice('da-DK', 'da-DK-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        DA_DK_WAVENET_C = Voice('da-DK', 'da-DK-Wavenet-C', SsmlVoiceGender.MALE, 24000)
        DA_DK_WAVENET_D = Voice('da-DK', 'da-DK-Wavenet-D', SsmlVoiceGender.FEMALE, 24000)
        DA_DK_WAVENET_E = Voice('da-DK', 'da-DK-Wavenet-E', SsmlVoiceGender.FEMALE, 24000)
        DE_DE_WAVENET_A = Voice('de-DE', 'de-DE-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        DE_DE_WAVENET_B = Voice('de-DE', 'de-DE-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        DE_DE_WAVENET_C = Voice('de-DE', 'de-DE-Wavenet-C', SsmlVoiceGender.FEMALE, 24000)
        DE_DE_WAVENET_D = Voice('de-DE', 'de-DE-Wavenet-D', SsmlVoiceGender.MALE, 24000)
        DE_DE_WAVENET_E = Voice('de-DE', 'de-DE-Wavenet-E', SsmlVoiceGender.MALE, 24000)
        DE_DE_WAVENET_F = Voice('de-DE', 'de-DE-Wavenet-F', SsmlVoiceGender.FEMALE, 24000)
        EL_GR_WAVENET_A = Voice('el-GR', 'el-GR-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        EN_AU_WAVENET_A = Voice('en-AU', 'en-AU-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        EN_AU_WAVENET_B = Voice('en-AU', 'en-AU-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        EN_AU_WAVENET_C = Voice('en-AU', 'en-AU-Wavenet-C', SsmlVoiceGender.FEMALE, 24000)
        EN_AU_WAVENET_D = Voice('en-AU', 'en-AU-Wavenet-D', SsmlVoiceGender.MALE, 24000)
        EN_GB_WAVENET_A = Voice('en-GB', 'en-GB-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        EN_GB_WAVENET_B = Voice('en-GB', 'en-GB-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        EN_GB_WAVENET_C = Voice('en-GB', 'en-GB-Wavenet-C', SsmlVoiceGender.FEMALE, 24000)
        EN_GB_WAVENET_D = Voice('en-GB', 'en-GB-Wavenet-D', SsmlVoiceGender.MALE, 24000)
        EN_GB_WAVENET_F = Voice('en-GB', 'en-GB-Wavenet-F', SsmlVoiceGender.FEMALE, 24000)
        EN_IN_WAVENET_A = Voice('en-IN', 'en-IN-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        EN_IN_WAVENET_B = Voice('en-IN', 'en-IN-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        EN_IN_WAVENET_C = Voice('en-IN', 'en-IN-Wavenet-C', SsmlVoiceGender.MALE, 24000)
        EN_IN_WAVENET_D = Voice('en-IN', 'en-IN-Wavenet-D', SsmlVoiceGender.FEMALE, 24000)
        EN_US_WAVENET_A = Voice('en-US', 'en-US-Wavenet-A', SsmlVoiceGender.MALE, 24000)
        EN_US_WAVENET_B = Voice('en-US', 'en-US-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        EN_US_WAVENET_C = Voice('en-US', 'en-US-Wavenet-C', SsmlVoiceGender.FEMALE, 24000)
        EN_US_WAVENET_D = Voice('en-US', 'en-US-Wavenet-D', SsmlVoiceGender.MALE, 24000)
        EN_US_WAVENET_E = Voice('en-US', 'en-US-Wavenet-E', SsmlVoiceGender.FEMALE, 24000)
        EN_US_WAVENET_F = Voice('en-US', 'en-US-Wavenet-F', SsmlVoiceGender.FEMALE, 24000)
        EN_US_WAVENET_G = Voice('en-US', 'en-US-Wavenet-G', SsmlVoiceGender.FEMALE, 24000)
        EN_US_WAVENET_H = Voice('en-US', 'en-US-Wavenet-H', SsmlVoiceGender.FEMALE, 24000)
        EN_US_WAVENET_I = Voice('en-US', 'en-US-Wavenet-I', SsmlVoiceGender.MALE, 24000)
        EN_US_WAVENET_J = Voice('en-US', 'en-US-Wavenet-J', SsmlVoiceGender.MALE, 24000)
        FIL_PH_WAVENET_A = Voice('fil-PH', 'fil-PH-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        FIL_PH_WAVENET_B = Voice('fil-PH', 'fil-PH-Wavenet-B', SsmlVoiceGender.FEMALE, 24000)
        FIL_PH_WAVENET_C = Voice('fil-PH', 'fil-PH-Wavenet-C', SsmlVoiceGender.MALE, 24000)
        FIL_PH_WAVENET_D = Voice('fil-PH', 'fil-PH-Wavenet-D', SsmlVoiceGender.MALE, 24000)
        FI_FI_WAVENET_A = Voice('fi-FI', 'fi-FI-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        FR_CA_WAVENET_A = Voice('fr-CA', 'fr-CA-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        FR_CA_WAVENET_B = Voice('fr-CA', 'fr-CA-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        FR_CA_WAVENET_C = Voice('fr-CA', 'fr-CA-Wavenet-C', SsmlVoiceGender.FEMALE, 24000)
        FR_CA_WAVENET_D = Voice('fr-CA', 'fr-CA-Wavenet-D', SsmlVoiceGender.MALE, 24000)
        FR_FR_WAVENET_A = Voice('fr-FR', 'fr-FR-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        FR_FR_WAVENET_B = Voice('fr-FR', 'fr-FR-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        FR_FR_WAVENET_C = Voice('fr-FR', 'fr-FR-Wavenet-C', SsmlVoiceGender.FEMALE, 24000)
        FR_FR_WAVENET_D = Voice('fr-FR', 'fr-FR-Wavenet-D', SsmlVoiceGender.MALE, 24000)
        FR_FR_WAVENET_E = Voice('fr-FR', 'fr-FR-Wavenet-E', SsmlVoiceGender.FEMALE, 24000)
        HI_IN_WAVENET_A = Voice('hi-IN', 'hi-IN-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        HI_IN_WAVENET_B = Voice('hi-IN', 'hi-IN-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        HI_IN_WAVENET_C = Voice('hi-IN', 'hi-IN-Wavenet-C', SsmlVoiceGender.MALE, 24000)
        HI_IN_WAVENET_D = Voice('hi-IN', 'hi-IN-Wavenet-D', SsmlVoiceGender.FEMALE, 24000)
        HU_HU_WAVENET_A = Voice('hu-HU', 'hu-HU-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        ID_ID_WAVENET_A = Voice('id-ID', 'id-ID-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        ID_ID_WAVENET_B = Voice('id-ID', 'id-ID-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        ID_ID_WAVENET_C = Voice('id-ID', 'id-ID-Wavenet-C', SsmlVoiceGender.MALE, 24000)
        ID_ID_WAVENET_D = Voice('id-ID', 'id-ID-Wavenet-D', SsmlVoiceGender.FEMALE, 24000)
        IT_IT_WAVENET_A = Voice('it-IT', 'it-IT-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        IT_IT_WAVENET_B = Voice('it-IT', 'it-IT-Wavenet-B', SsmlVoiceGender.FEMALE, 24000)
        IT_IT_WAVENET_C = Voice('it-IT', 'it-IT-Wavenet-C', SsmlVoiceGender.MALE, 24000)
        IT_IT_WAVENET_D = Voice('it-IT', 'it-IT-Wavenet-D', SsmlVoiceGender.MALE, 24000)
        JA_JP_WAVENET_A = Voice('ja-JP', 'ja-JP-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        JA_JP_WAVENET_B = Voice('ja-JP', 'ja-JP-Wavenet-B', SsmlVoiceGender.FEMALE, 24000)
        JA_JP_WAVENET_C = Voice('ja-JP', 'ja-JP-Wavenet-C', SsmlVoiceGender.MALE, 24000)
        JA_JP_WAVENET_D = Voice('ja-JP', 'ja-JP-Wavenet-D', SsmlVoiceGender.MALE, 24000)
        KO_KR_WAVENET_A = Voice('ko-KR', 'ko-KR-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        KO_KR_WAVENET_B = Voice('ko-KR', 'ko-KR-Wavenet-B', SsmlVoiceGender.FEMALE, 24000)
        KO_KR_WAVENET_C = Voice('ko-KR', 'ko-KR-Wavenet-C', SsmlVoiceGender.MALE, 24000)
        KO_KR_WAVENET_D = Voice('ko-KR', 'ko-KR-Wavenet-D', SsmlVoiceGender.MALE, 24000)
        NB_NO_WAVENET_A = Voice('nb-NO', 'nb-NO-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        NB_NO_WAVENET_B = Voice('nb-NO', 'nb-NO-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        NB_NO_WAVENET_C = Voice('nb-NO', 'nb-NO-Wavenet-C', SsmlVoiceGender.FEMALE, 24000)
        NB_NO_WAVENET_D = Voice('nb-NO', 'nb-NO-Wavenet-D', SsmlVoiceGender.MALE, 24000)
        NB_NO_WAVENET_E = Voice('nb-NO', 'nb-no-Wavenet-E', SsmlVoiceGender.FEMALE, 24000)
        NL_NL_WAVENET_A = Voice('nl-NL', 'nl-NL-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        NL_NL_WAVENET_B = Voice('nl-NL', 'nl-NL-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        NL_NL_WAVENET_C = Voice('nl-NL', 'nl-NL-Wavenet-C', SsmlVoiceGender.MALE, 24000)
        NL_NL_WAVENET_D = Voice('nl-NL', 'nl-NL-Wavenet-D', SsmlVoiceGender.FEMALE, 24000)
        NL_NL_WAVENET_E = Voice('nl-NL', 'nl-NL-Wavenet-E', SsmlVoiceGender.FEMALE, 24000)
        PL_PL_WAVENET_A = Voice('pl-PL', 'pl-PL-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        PL_PL_WAVENET_B = Voice('pl-PL', 'pl-PL-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        PL_PL_WAVENET_C = Voice('pl-PL', 'pl-PL-Wavenet-C', SsmlVoiceGender.MALE, 24000)
        PL_PL_WAVENET_D = Voice('pl-PL', 'pl-PL-Wavenet-D', SsmlVoiceGender.FEMALE, 24000)
        PL_PL_WAVENET_E = Voice('pl-PL', 'pl-PL-Wavenet-E', SsmlVoiceGender.FEMALE, 24000)
        PT_BR_WAVENET_A = Voice('pt-BR', 'pt-BR-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        PT_PT_WAVENET_A = Voice('pt-PT', 'pt-PT-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        PT_PT_WAVENET_B = Voice('pt-PT', 'pt-PT-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        PT_PT_WAVENET_C = Voice('pt-PT', 'pt-PT-Wavenet-C', SsmlVoiceGender.MALE, 24000)
        PT_PT_WAVENET_D = Voice('pt-PT', 'pt-PT-Wavenet-D', SsmlVoiceGender.FEMALE, 24000)
        RU_RU_WAVENET_A = Voice('ru-RU', 'ru-RU-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        RU_RU_WAVENET_B = Voice('ru-RU', 'ru-RU-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        RU_RU_WAVENET_C = Voice('ru-RU', 'ru-RU-Wavenet-C', SsmlVoiceGender.FEMALE, 24000)
        RU_RU_WAVENET_D = Voice('ru-RU', 'ru-RU-Wavenet-D', SsmlVoiceGender.MALE, 24000)
        RU_RU_WAVENET_E = Voice('ru-RU', 'ru-RU-Wavenet-E', SsmlVoiceGender.FEMALE, 24000)
        SK_SK_WAVENET_A = Voice('sk-SK', 'sk-SK-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        SV_SE_WAVENET_A = Voice('sv-SE', 'sv-SE-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        TR_TR_WAVENET_A = Voice('tr-TR', 'tr-TR-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        TR_TR_WAVENET_B = Voice('tr-TR', 'tr-TR-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        TR_TR_WAVENET_C = Voice('tr-TR', 'tr-TR-Wavenet-C', SsmlVoiceGender.FEMALE, 24000)
        TR_TR_WAVENET_D = Voice('tr-TR', 'tr-TR-Wavenet-D', SsmlVoiceGender.FEMALE, 24000)
        TR_TR_WAVENET_E = Voice('tr-TR', 'tr-TR-Wavenet-E', SsmlVoiceGender.MALE, 24000)
        UK_UA_WAVENET_A = Voice('uk-UA', 'uk-UA-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        VI_VN_WAVENET_A = Voice('vi-VN', 'vi-VN-Wavenet-A', SsmlVoiceGender.FEMALE, 24000)
        VI_VN_WAVENET_B = Voice('vi-VN', 'vi-VN-Wavenet-B', SsmlVoiceGender.MALE, 24000)
        VI_VN_WAVENET_C = Voice('vi-VN', 'vi-VN-Wavenet-C', SsmlVoiceGender.FEMALE, 24000)
        VI_VN_WAVENET_D = Voice('vi-VN', 'vi-VN-Wavenet-D', SsmlVoiceGender.MALE, 24000)


# Enum generation from Google Cloud API
def _generate_standard_voice_enums():
    voices = {_format_enum(voice) for voice in _all_voices()
              if 'standard' in voice.name.lower()}
    return sorted(voices)


def _generate_wavenet_voice_enums():
    voices = {_format_enum(voice) for voice in _all_voices()
              if 'wavenet' in voice.name.lower()}
    return sorted(voices)


def _all_voices():
    client = tts.TextToSpeechClient()
    response = client.list_voices()
    return response.voices


def _format_enum(voice):
    languages = ', '.join(voice.language_codes)
    name = voice.name
    gender = voice.ssml_gender
    rate = voice.natural_sample_rate_hertz

    member_name = '_'.join(name.upper().split('-'))

    formatted = (f"{member_name} = Voice('{languages}', "
                 f"'{name}', SsmlVoiceGender.{gender.name}, {rate})")
    return formatted


def main():
    print(f'\tclass Standard(enum.Enum):')
    for member in _generate_standard_voice_enums():
        print(f'\t\t{member}')
    print(f'\tclass WaveNet(enum.Enum):')
    for member in _generate_wavenet_voice_enums():
        print(f'\t\t{member}')


if __name__ == '__main__':
    main()