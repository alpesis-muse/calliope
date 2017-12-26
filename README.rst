##############################################################################
Calliope
##############################################################################

==============================================================================
Features
==============================================================================

- Randomly choosing a word from the vocabulary list
- Speaking out the word with Text-To-Speech
- Translating the word (TODO)

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
