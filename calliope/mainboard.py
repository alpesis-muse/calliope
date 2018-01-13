from games.vocabulary_reminder import VocabularyReminder

GAME_LIST = """
    Game List:
    - 1. Vocabulary Reminder
    - 2. Article Reader
    - 0: exit
    Please enter 1 or 2 to choose the game, 0 to exit:  
"""

def mainboard():
    while True:
        key = raw_input(GAME_LIST)
        if key == "0":
            print("Exit.")
            exit(0)

        elif key == "1":
            vocab_reminder = VocabularyReminder()
            vocab_reminder.run()

        else:
            print("Please enter 1 or 2: ")
