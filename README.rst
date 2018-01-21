##############################################################################
Calliope
##############################################################################

Calliope is a bot for fun.

==============================================================================
Features
==============================================================================

Games:

- VocabularyReminder
    - multiple languages support (TODO)
    - composing the sentenses by inserting the words (TODO)
- ArticleReader
- MusicPlayer
    - randomly playing the music (TODO)
    - selecting the music and show the link (TODO)
- GiftSelector
- Daily news (TODO)

==============================================================================
Getting Started
==============================================================================

Prequisites:

- OSX
- virtualenv

How it runs:

::

    # installing the requirements
    $ mkvirtualenv calliope
    $ pip install -r requirements/base.txt

    # run
    $ cd calliope
    $ python main.py

Calliope

::

    Game List:
    - 1. Vocabulary Reminder
    - 2. Article Reader
    - 3. Music Player
    Please choose a game [enter index, or q to exit]:
    1
    Welcome to Vocabulary Reminder!
    Please enter [n: next, q: quit]: n
    saltwater fishing
    盐水捕鱼
    Please enter [n: next, q: quit]: q


Creating your custom vocabularies or articles:

::

    $ vim calliope/data/vocabularies/<xxx.txt>
    # adding a word or some words line by line

    $ vim calliope/data/articles/<xxx.txt>
    # adding the contents
