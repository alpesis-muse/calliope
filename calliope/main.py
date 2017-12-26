if __name__ == '__main__':
    vocabularies = open('data/vocabularies.txt', 'rb')
    for vocabulary in vocabularies.readlines():
        print vocabulary.strip()
