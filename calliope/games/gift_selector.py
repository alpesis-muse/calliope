import os
import yaml

from settings import GIFTS_DIR


class GiftSelector:

    def __init__(self):
        self.gifts = []
        self.data = []

    def run(self):
        print("Welcome to Gift Selector!")
        self._prepare()

        print("Gift List:")
        for i in range(len(self.data)):
            for gift in self.data[i]:
                print "- {0}".format(gift)
                for item in self.data[i][gift]:
                    print "  - {0}".format(self.data[i][gift][item]["item"])

    def _prepare(self):
        for gift in os.listdir(GIFTS_DIR):
            self.gifts.append(gift)
            data = yaml.safe_load(open(GIFTS_DIR+gift))
            self.data.append(data)
