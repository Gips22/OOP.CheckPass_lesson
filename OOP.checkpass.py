from string import ascii_lowercase, ascii_uppercase, digits
from random import randint


class EmailValidator:
    SIMBOLS = ascii_lowercase + ascii_uppercase + digits + '._@'
    SIMBOLS1 = ascii_lowercase + ascii_uppercase + digits + '._'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if not set(email) < set(cls.SIMBOLS):
            return False
        s = email.split('@')
        if len(s) != 2:
            return False
        if len(s[0]) > 100 or len(s[1]) > 50:
            return False
        if '.' not in s[1]:
            return False
        if email.count('..') > 0:
            return False
        return True

    @staticmethod
    def __is_email_str(email):
        if type(email) != str:
            return False
        return True

    @classmethod
    def get_random_email(cls):
        n = randint(4, 20)
        length = len(cls.SIMBOLS1) - 1
        return ''.join(cls.SIMBOLS1[randint(0, length)] for i in range(n)) + '@gmail.com'
