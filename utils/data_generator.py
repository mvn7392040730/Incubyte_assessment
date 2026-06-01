import time
import random
import string


def generate_username():
    return f"user_{int(time.time())}"


def generate_password(length=12):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for ch in range(length))


def generate_user():
    return {
        "username": generate_username(),
        "password":generate_password()}