from numb3rs import validate
def main():
    test_validate()

def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("200.24.0.255") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.256") == False
    assert validate("255.255.255") == False
    assert validate("255.255.255255") == False
    assert validate("255.255.255.-255") == False
    assert validate("255249.255.255.255") == False
    assert validate("1.2.3.1000") == False
    assert validate("127.0.0.1") == True



if __name__ == "__main__":
    main()