from um import count

def test_count():
    assert count('um') == 1
    assert count('um?') == 1
    assert count('Um, thanks for your time.') == 1
    assert count('Um, it was great to see you, um...') == 2
    assert count('mummi') == 0