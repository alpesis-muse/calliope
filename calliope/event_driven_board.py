from games.vocabulary_reminder import VocabularyReminder
from games.article_reader import ArticleReader
from games.music_player import MusicPlayer
from games.gift_selector import GiftSelector


GAME_LIST = """
Game list:
- 1. Vocabulary Reminder
- 2. Article Reader
- 3. Music Player
- 4. Gift Selector
Please choose a game [enter index, or q to exit]:
"""


class EventDrivenBoard:

    def __init__(self):
        self.onboard()
        
        self.accepted_messages = {}
        self.register_callback("1", self.vocabulary_reminder)
        self.register_callback("2", self.article_reader)
        self.register_callback("3", self.music_player)
        self.register_callback("4", self.gift_selector)
        self.register_callback("q", self.quit)


    def onboard(self):
        print(GAME_LIST)


    def play(self):
        while True:
            key = raw_input(GAME_LIST)
            self.handle_message(key)


    def register_callback(self, message, callback):
        if message not in self.accepted_messages:
            self.accepted_messages[message] = []
        self.accepted_messages[message].append(callback)


    def vocabulary_reminder(self):
        vocab_reminder = VocabularyReminder()
        vocab_reminder.run()


    def article_reader(self):
        article_reader = ArticleReader()
        article_reader.run()


    def music_player(self):
        music_player = MusicPlayer()
        music_player.run()


    def gift_selector(self):
        gift_selector = GiftSelector()
        gift_selector.run()


    def quit(self):
        exit(0);


    def handle_message(self, message):
        if message not in self.accepted_messages:
            print("Sorry, I don't understand", message)
        else:
            callbacks = self.accepted_messages[message]
            for callback in callbacks:
                callback()
