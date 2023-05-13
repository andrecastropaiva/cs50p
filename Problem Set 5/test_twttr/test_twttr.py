from twttr import shorten


# test lowercase
def test_lowercase():
    assert shorten("Hello World") == "Hll Wrld"
    assert shorten("aeiou") == ""

# test upper case
def test_uppercase():
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("AEIOU") == ""

# test no vowels
def test_no_vowels():
    assert shorten("tst n vwls") == "tst n vwls"

# test numbers
def test_numbers():
    assert shorten('1234') == '1234'

# test punctuation
def test_punctuation():
    assert shorten('!?-_.,') == '!?-_.,'


# main engine to run all functions
def main():
# Test functions call
    test_lowercase()
    test_uppercase()
    test_no_vowels()
    test_numbers()
    test_punctuation()


if __name__ == '__main__':
    main()