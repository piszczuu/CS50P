from numb3rs import validate


def main():
    test_validate_correct()
    test_validate_incorrect()


def test_validate_correct():
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True


def test_validate_incorrect():
    assert validate("1.1.01.1") == False
    assert validate("1.1.256.1000") == False
    assert validate("512.1.001.1") == False
    assert validate("cat") == False
