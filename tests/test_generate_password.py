from email import charset
from string import punctuation
import string
import pytest
from app.generate_password import generate_password
from app.exceptions import PasswordTooLongException, PasswordTooShortException, InvalidCharsetException


def test_password_default_length():
    assert len(generate_password()) == 8

def test_password_too_short():
    with pytest.raises(PasswordTooShortException):
        generate_password(pass_length=5)

def test_password_too_long():
    with pytest.raises(PasswordTooLongException):
        generate_password(pass_length=33)

def test_valid_charset():
    with pytest.raises(InvalidCharsetException):
        generate_password(charset_chosen=["invalid charset"], pass_length=8)

def test_password_contains_one_lower():
        assert any(password_char.islower for password_char in generate_password())

def test_password_contains_one_upper():
        assert any(password_char.isupper for password_char in generate_password())

def test_password_contains_one_digit():
        assert any(password_char.isdigit for password_char in generate_password())

def test_password_contains_one_punctuation():
        assert any(password_char in string.punctuation for password_char in generate_password())
                