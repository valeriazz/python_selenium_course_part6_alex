import pytest


def test_sending_mail_1(set_up, some):
    print('Письмо отправлено')


def test_sending_mail_2(set_up, some):
    print('Письмо отправлено')

# pytest -s -v: если хотим выполнить все тесты из всех файлов; pytest -s -v test_mail.py: если хотим выполнить один
# файлt
# ключ -v выводит назв.файла, название теста, результат и %
# ключ -s выводит назв.файла и принты
# ключ -s -v выводит назв.файла, название теста, принты и результат

