##############################################################################
Calliope
##############################################################################

Calliope is a bot for fun.

==============================================================================
Features
==============================================================================

- Randomly choosing a word from the vocabulary list
- Voice
    - pronouncing the word shown with text-to-speech library
    - text-to-speech with linux support (TODO)
- Translation
    - translating a word from English to Chinese
    - multiple languages support (TODO)
- Composing the sentences by inserting the words (TODO)
- Daily news (TODO)
- Music Albums (TODO)

==============================================================================
Getting Started
==============================================================================

Prequisites:

- virtualenv

How it runs:

::

    # installing the requirements
    $ mkvirtualenv calliope
    $ pip install -r requirements/base.txt

    # run
    $ cd calliope
    $ python main.py

Game looks like:

::

	Please enter [n: next, q: quit]: n
	mammal
	Please enter [n: next, q: quit]: n
	proponent
	Please enter [n: next, q: quit]: n
	watercraft
	Please enter [n: next, q: quit]: n
	mammal
	Please enter [n: next, q: quit]: n
	Alaska Peninsula
	Please enter [n: next, q: quit]: n
	retreat
	Please enter [n: next, q: quit]: n
	a southerly direction
	Please enter [n: next, q: quit]: q


Creating your custom vocabularies:

::

    $ vim calliope/data/vocabularies.txt
    $ adding a word or some words line by line
