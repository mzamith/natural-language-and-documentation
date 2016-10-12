"""
====================
NLTK Simple Example
====================
"""

import nltk

phrase = "yellw dg barked at the cat."


def tokenize(sentence):

    """ Tokenize Function - Devide a sentence into its words
    Args:
        sentence (str): The sample sentence to devide into tokens
    Returns:
        list of str: List of tokens
    """
    tokens = nltk.word_tokenize(sentence)
    print tokens
    return tokens


def tag(tokens):

    """ Tag Function - Tag a sample of tokens
    Args:
        tokens (list of string): list of tokens to tag
    Returns:
        list of tupples: each tupple is a string (token) and its tag
    """
    tagged = nltk.pos_tag(tokens)
    return tagged


def chunk(tagged):

    """ Chunk Function - Group tokens according to regex
    Args:
        tagged (list of tupples): list of tagged tokens to chunk
    Returns:
        tree: returns a tree element
    """
    grammar = "ENTITY: {<DT>?<JJ>*<NN>}"
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(tagged)
    return result


chunk(tag(tokenize(phrase))).draw();
