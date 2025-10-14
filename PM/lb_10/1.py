import re
from typing import List

def is_valid_email(email):
    if bool(re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)):
        return 'email соответствует шаблону'
    return 'email не соответствует шаблону'
