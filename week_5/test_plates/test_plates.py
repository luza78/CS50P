from plates import is_valid

def test_len():
    assert is_valid("AAEWQT") == True
    assert is_valid("EART") == True
    assert is_valid("ARMONDS") == False
    assert is_valid("AA") == True
    assert is_valid("B") == False
    assert is_valid("BAER02") == False
    assert is_valid("7AAER") == False
    assert is_valid("50CS") == False
    assert is_valid("555550") == False


def test_num():
    assert is_valid("AAEWQ7") == True
    assert is_valid("ECHO1Y") == False
    assert is_valid("A2EWQ3") == False
    assert is_valid("ECHO69") == True

def test_case():
    assert is_valid("BrexiT") == True
    assert is_valid("aaemrt") == True
    assert is_valid("AMstel") == True

def test_sym():
    assert is_valid("AAEWQ!") == False
    assert is_valid("BAN!HA") == False
    assert is_valid("ARGHH!!") == False
    assert is_valid("?whotf") == False