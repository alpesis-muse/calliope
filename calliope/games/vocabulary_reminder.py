import os
import random

from settings import VOCABULARIES_DIR
from settings import LANGUAGE_SPEAKERS
#from translator import Translator
from googletrans import Translator


class VocabularyReminder:

    def __init__(self):
        self.vocabularies = []
        self.translator = Translator()

    def run(self):
        print("Welcome to Vocabulary Reminder!")
        self._prepare()

        while (1):
            key = raw_input("Please enter [n: next, q: quit]: ")

            if key == "q":
                exit(0)

            elif key == "n":
                idx = random.randint(0, len(self.vocabularies)-1)
                word = self.vocabularies[idx].strip()
                print word
                os.system('say -v {0} {1}'.format(LANGUAGE_SPEAKERS["en_US"][-3], word))
                word_translated = self.translator.translate(word, dest='zh-cn')
                print word_translated.text.encode('utf-8')

    def _prepare(self):
        for txt in os.listdir(VOCABULARIES_DIR):
            words = open(VOCABULARIES_DIR+txt, 'rb').readlines()
            self.vocabularies.extend(words)
            
