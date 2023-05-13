from working import convert
import pytest


def main():
    test_new_format()
    test_wrong_new_format()
    test_wrong_hours()
    test_wrong_minutes()



def test_new_format():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'



def test_wrong_new_format():
    with pytest.raises(ValueError):
        convert('13 PM to 3 PM')




def test_wrong_hours():
    with pytest.raises(ValueError):
        convert('9 AM - 16 PM')



def test_wrong_minutes():
    with pytest.raises(ValueError):
        convert('9 AM - 4 PM')


