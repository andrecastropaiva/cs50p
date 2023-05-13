import pytest # needed for testing ZeroDivisionError and ValueError
from fuel import convert, gauge # from the name of the file 'fuel' import the functions


# Test input
def test_input():
    # 1/5 is 20% ... result has to be the same for both functions (convert(), gauge())but also have to compare gauge() against letter
    assert convert('1/5') == 20 and gauge(20) == '20%'
    # 2/200 is 1% ... result has to be the same for both functions (convert(), gauge())but also have to compare gauge() against letter
    assert convert('2/200') == 1 and gauge(1) == 'E'
    # 99/100 is 99% ... result has to be the same for both functions (convert(), gauge())but also have to compare gauge() against letter
    assert convert('99/100') == 99 and gauge(99) == 'F'



# test ValueError
def test_value_error():
    with pytest.raises(ValueError):
        convert('you/me')





# Test ZeroDivisionError
def test_zero_division_error():
    # using raises() from pytest to check if the code raises a ZeroDivisionError exception
    with pytest.raises(ZeroDivisionError):
        convert('5 / 0') # this is the function we use to do the calculations (convert())





# Engine to run the call back functions
def main():
    test_input()
    test_value_error()
    test_zero_division_error()

if __name__ == '__main__':
    main()