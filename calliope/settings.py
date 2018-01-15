# ----------------------------------------------------------------------------
# Data

VOCABULARIES_DIR = "data/vocabularies/"
ARTICLES_DIR = "data/articles/"
ALBUMS_DIR = "data/albums/"

# ----------------------------------------------------------------------------
# Voice

# ref: https://apple.stackexchange.com/questions/3454/say-in-different-language
LANGUAGE_SPEAKERS = {
  "en_US": ["Alex", "Bahh", "Bells", "Boing", "Bruce", "Bubbles",
            "Cellos", "Deranged", "Fred", "Hysterical", "Junior", "Kathy", "Princess",
            "Ralph", "Samantha", "Trinoids", "Victoria", "Whisper", "Zarvox"],
  "en_GB": ["Daniel"],
  "en_AU": ["Karen"],
  "en_IE": ["Moira"],
  "en_IN": ["Veena"],
  "en_ZA": ["Tessa"],
  "el_GR": ["Melina"],
  "es_ES": ["Monica"],
  "es_MX": ["Paulina"],
  "da_DK": ["Sara"],
  "fi_FI": ["Satu"],
  "fr_FR": ["Thomas"],
  "it_IT": ["Alice"],
  "sv_SE": ["Alva"],
  "fr_CA": ["Amelie"],
  "de_DE": ["Anna"],
  "he_IL": ["Carmit"],
  "id_ID": ["Damayanti"],
  "es_AR": ["Diego"],
  "nl_BE": ["Ellen"],
  "ro_RO": ["Ioana"],
  "pt_PT": ["Joana"],
  "pt_BR": ["Luciana"],
  "th_TH": ["Kanya"],
  "ja_JP": ["Kyoko"],
  "sk_SK": ["Laura"],
  "hi_IN": ["Lekha"],
  "ar_SA": ["Maged"],
  "hu_HU": ["Mariska"],
  "zh_CN": ["Ting-Ting"],
  "zh_TW": ["Mei-Jia"],
  "zh_HK": ["Sin-ji"],
  "ru_RU": ["Milena"],
  "nb_NO": ["Nora"],
  "ko_KR": ["Yuna"],
  "nl_NL": ["Xander"],
  "tr_TR": ["Yelda"],
  "pl_PL": ["Zosia"],
  "cs_CZ": ["Zuzana"]
}


# ----------------------------------------------------------------------------
# Translator

# translator server headers
TRANSLATOR_HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19'}
# translator server url
TRANSLATOR_URL = 'http://mymemory.translated.net/api/get?q=%s&langpair=%s|%s'
# text limit: # of charactors input
TRANSLATOR_TEXT_LIMIT = 1000
