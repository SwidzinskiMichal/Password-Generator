class PasswordTooShortException(Exception):
    pass


class PasswordTooLongException(Exception):
    pass


class InvalidCharsetException(Exception):
    pass


class EmptyCharsetException(Exception):
    pass