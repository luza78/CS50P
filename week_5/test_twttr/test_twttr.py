from twttr import shorten


def test_upper():
    assert shorten("twitter") == "twttr"
    assert shorten("twItTer") == "twtTr"


def test_num():
    assert shorten("t1tt3r") == "t1tt3r"
    assert shorten("Twitt3R Iz c00l") == "Twtt3R z c00l"


def test_sym():
    assert shorten("y r y0 m4d Br0?!") == "y r y0 m4d Br0?!"
    assert shorten("IT'S SO HOT RN ?") == "T'S S HT RN ?"
