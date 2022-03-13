from password_generator import password_generator

def test_password_default_length():
    assert len(password_generator()) == 8

 