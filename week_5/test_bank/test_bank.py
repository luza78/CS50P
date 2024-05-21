from bank import value

def test_plain():
    assert value("hello") == 0
    assert value("hello there") == 0
    assert value("howdy partner") == 20
    assert value("nice to meet ya") == 100

def test_upperlower():
    assert value("HEY") == 20
    assert value("HellO JOhn") == 0
    assert value("WHAT'S UP DOC?") == 100

def test_numsym():
    assert value("HEY!") == 20
    assert value("BUT WHY?!") == 100
