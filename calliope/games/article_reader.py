import os

from settings import ARTICLES_DIR
from settings import LANGUAGE_SPEAKERS


class ArticleReader:

    def __init__(self):
        self.articles = []

        print("Welcome to Article Reader!")

    def run(self):
        self._prepare()
        self._control()


    def _control(self):
        print("Article List:")
        for index, article in enumerate(self.articles):
            print "- {0}. {1}".format(str(index), article)
        key = raw_input("Please choose an article [enter index, q to exit]: ")

        if key == "q":
            exit(0)

        else:
            filename = ARTICLES_DIR + self.articles[int(key)]
            article = open(filename, "rb")
            for line in article.readlines():
                line = line.strip()
                if len(line) > 0:
                    print line
                    os.system("say -v {0} {1}".format(LANGUAGE_SPEAKERS["en_US"][0], line.strip()))


    def _prepare(self):
       for article in os.listdir(ARTICLES_DIR):
           self.articles.append(article)
