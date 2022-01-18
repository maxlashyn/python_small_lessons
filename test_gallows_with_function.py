from gallows_with_functions import Word


def test_word_initialization():
    example = 'привет'
    word = Word(example)

    assert word.chars == list(example)
    assert word.guess_chars == ['_' for i in range(0, len(example))]

def test_fill_chars():
    example = 'привет'
    word = Word(example)

    current = word.guess_chars.copy()
    word.fill_chars('г')
    assert word.guess_chars == current

    word.fill_chars('п')
    current[0] = 'п'
    assert word.guess_chars == current

def test_in_word():
    example = 'привет'
    word = Word(example)

    assert word.in_word('р')
    assert word.in_word('ы') is False

def test_is_complete():
    example = 'привет'
    word = Word(example)

    assert word.is_complete() is False
    word.guess_chars = list(example)
    assert word.is_complete()