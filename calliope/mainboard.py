from games.vocabulary_reminder import VocabularyReminder
from games.article_reader import ArticleReader

GAME_LIST = """
Game List:
- 1. Vocabulary Reminder
- 2. Article Reader
Please enter 1 or 2 to choose the game, q to exit:  
"""

def mainboard():
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

        else:
            print("Please enter 1 or 2: ")
