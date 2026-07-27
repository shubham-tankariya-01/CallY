import string
import random

char_list = string.ascii_uppercase
digit_list = string.digits

final = char_list + digit_list

def room_code()->str:
    chars = ''.join(random.choice(final) for _ in range(6))
    return f"{chars[:3]}-{chars[3:]}"

