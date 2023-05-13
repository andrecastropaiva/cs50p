from numb3rs import validate

def main():
    test_iptrue()
    test_ipfalse()

def test_iptrue():
    assert validate('123.123.123.123') == True
    assert validate('12.22.2.123') == True

def test_ipfalse():
    assert validate('cat') == False
    assert validate('123.1234.1234.1234') == False
    assert validate('1.300.350.400') == False


if __name__ == "__main__":
    main()