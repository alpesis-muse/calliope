import os
import random


if __name__ == '__main__':

    vocabularies = open('data/vocabularies.txt', 'rb').readlines()

    while (1):
        key = raw_input("Please enter [n: next, q: quit]: ")

        if key == "q":
            exit(0)

        elif key == "n":
            idx = random.randint(0, len(vocabularies)-1)
            word = vocabularies[idx].strip()
            print word
            os.system('say {0}'.format(word))
