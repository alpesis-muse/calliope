import os
import yaml

from settings import ALBUMS_DIR


class MusicPlayer:

    def __init__(self):
        self.albums = []
        self.data = []

    def run(self):
        print("Welcome to Music Player!")
        self._prepare()

        print("Album List:")
        for i in range(len(self.data)):
            for album in self.data[i]:
                print "- {0}".format(album)
                for song in self.data[i][album]:
                    print "  - {0}".format(self.data[i][album][song]["title"])


    def _prepare(self):
        for album in os.listdir(ALBUMS_DIR):
            self.albums.append(album)
            data = yaml.safe_load(open(ALBUMS_DIR+album))
            self.data.append(data)
