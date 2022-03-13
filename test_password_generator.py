import pytest
from password_generator import PasswordTooLongException, PasswordTooShortException, password_generator

def test_password_default_length():
    assert len(password_generator()) == 8

def test_password_too_short():
    with pytest.raises(PasswordTooShortException):
        password_generator(5)

def test_password_too_long():
    with pytest.raises(PasswordTooLongException):
        password_generator(33)
        