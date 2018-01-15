from games.vocabulary_reminder import VocabularyReminder
from games.article_reader import ArticleReader
from games.music_player import MusicPlayer

GAME_LIST = """
Game List:
- 1. Vocabulary Reminder
- 2. Article Reader
- 3. Music Player
Please choose a game [enter index, or q to exit]:  
"""

def board():
    while True:
        key = raw_input(GAME_LIST)
        if key == "q":
            print("Exit.")
            exit(0)

        elif key == "1":
            vocab_reminder = VocabularyReminder()
            vocab_reminder.run()

        elif key == "2":
            article_reader = ArticleReader()
            article_reader.run()

        elif key == "3":
            music_player = MusicPlayer()
            music_player.run()

        else:
            print("Please enter 1 or 2: ")
