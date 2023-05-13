from bank import value


# test return 0
def test_zero():
    assert value('hello andre') == 0
    assert value('Hello') == 0
    assert value('HeLlo Andre') == 0


# test return 20
def test_twenty():
    assert value('hey andre') == 20
    assert value('Hey') == 20
    assert value('HeY Andre') == 20

# test return 100
def test_hundred():
    assert value('whatever you want') == 100
    assert value('Xyz') == 100
    assert value('YoU Man') == 100


# Engine to call back function
def main():
    test_zero()
    test_twenty()
    test_hundred()


if __name__ == '__main__':
    main()