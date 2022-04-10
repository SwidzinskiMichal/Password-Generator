from string import punctuation
import string
import pytest
from app.password_generator import password_generator
from app.exceptions import PasswordTooLongException, PasswordTooShortException

def test_password_default_length():
    assert len(password_generator()) == 8

def test_password_too_short():
    with pytest.raises(PasswordTooShortException):
        password_generator(pass_length=5)

def test_password_too_long():
    with pytest.raises(PasswordTooLongException):
        password_generator(pass_length=33)

def test_password_contains_one_lower():
        assert any(password_char.islower for password_char in password_generator())

def test_password_contains_one_upper():
        assert any(password_char.isupper for password_char in password_generator())

def test_password_contains_one_digit():
        assert any(password_char.isdigit for password_char in password_generator())

def test_password_contains_one_punctuation():
        assert any(password_char in string.punctuation for password_char in password_generator())
                