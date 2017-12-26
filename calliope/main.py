import random


if __name__ == '__main__':
    vocabularies = open('data/vocabularies.txt', 'rb').readlines()
    idx = random.randint(0, len(vocabularies))
    print vocabularies[idx]
    #for vocabulary in vocabularies.readlines():
    #    print vocabulary.strip()
