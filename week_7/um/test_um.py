from um import count

def main():
    test_none()
    test_lower()
    test_upper()

def test_none():
    assert count("Winnie the poo is a yummy bunny") == 0
    assert count("Ice cream go YumYum lick lick") == 0

def test_lower():
    assert count("You see, um, the thing is um, how do you say um...") == 3
    assert count("What to um, say?") == 1
    assert count("humans are um, monkeys if you um, think about it!") == 2

def test_upper():
    assert count("FOR SOME REASON UM, I'M UM, REALLY LOUD, UM, YEAH!") == 3
    assert count("YUMTUMBUM, THIS WILL BE FUN") == 0
    assert count("HUM, HUM, HUM, I'M A BEAVER") == 0


if __name__ == "__main__":
    main()