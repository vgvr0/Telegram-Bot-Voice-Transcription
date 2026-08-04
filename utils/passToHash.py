import bcrypt


def toHash(password):
    # Кодируем входящую строку в байты
    password_bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()
    # Хешируем и ВОЗВРАЩАЕМ результат
    return bcrypt.hashpw(password_bytes, salt)


def ExaminationHash(enter_passwd, hashed):
    # Кодируем введенный пароль в байты перед проверкой
    enter_passwd_bytes = enter_passwd.encode('utf-8')

    if bcrypt.checkpw(enter_passwd_bytes, hashed):
        return True
    else:
        return False


if __name__ == '__main__':
    # 1. Хешируем нужный нам пароль
    hashed = toHash('plat')


    print(hashed)
    # 2. Проверяем (выведет: Неверный пароль!)
    ExaminationHash('alksdjf', hashed)

    # 3. Проверяем правильным (выведет: Пароль верный!)
    ExaminationHash('very strong password', hashed)