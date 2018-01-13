import os
import random

from settings import DATA_LIST
from settings import LANGUAGE_SPEAKERS
from translator import Translator


class VocabularyReminder:

    def __init__(self):
        self.vocabularies = []
        self.locale = Translator() 

        print("Welcome to Vocabulary Reminder!")

    def run(self):
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
                word_translated = self.locale.translate(word)
                print word_translated

    def _prepare(self):
        for txt in DATA_LIST:
            words = open(txt, 'rb').readlines()
            self.vocabularies.extend(words)
            
