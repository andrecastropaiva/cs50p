from plates import is_valid

# test max of 6 characters (letters or numbers) and a minimum of 2 characters
def test_min_max_characters_match():
    assert is_valid('A') == False
    assert is_valid('APACAS') == True
    assert is_valid('aP3451') == True
    assert is_valid('AP') == True
    assert is_valid('AAAAP34512') == False


# test if characters at position 0 and 1 are letters (first 2 characters must be letters)
def test_zero_one_position_characters_letters_only():
    assert is_valid('55') == False
    assert is_valid('AB') == True
    assert is_valid('B2') == False
    assert is_valid('ba') == True
    assert is_valid('5c') == False



# test if characters after the letters only contain numbers
def test_after_letters_numbers_only():
    assert is_valid('AA1234') == True
    assert is_valid('AP55AS') == False
    assert is_valid('aP0451') == False
    assert is_valid('ap1234') == True




# test if characters at the end of string are numbers and the first of those numbers isn't zero
def test_last_char_are_numbers():
    assert is_valid('AA07') == False
    assert is_valid('AP70') == True
    assert is_valid('aP34') == True




# test for only letters and numbers (no symbols or spaces)
def test_letters_numbers_only():
    assert is_valid('XY.1234') == False
    assert is_valid('ZC123!') == False
    assert is_valid('aP3451') == True
    assert is_valid('?AP111') == False
    assert is_valid('AA123 ') == False # has space



# Engine to call all functions back
def main():
    test_min_max_characters_match()
    test_zero_one_position_characters_letters_only()
    test_after_letters_numbers_only()
    test_last_char_are_numbers()
    test_letters_numbers_only()

if __name__ == '__main__':
    main()