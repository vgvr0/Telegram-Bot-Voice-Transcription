import bcrypt


def ExaminationHash(symbol, hashed):
    return bcrypt.checkpw(symbol.encode(), hashed)
