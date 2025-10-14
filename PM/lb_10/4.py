import re
from typing import List

def is_strong_password(password: str) -> bool:
    if 8 >= len(password) <= 20:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[@#$%^&+=.]', password):
        return False
    return True
