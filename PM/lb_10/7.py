import re
from typing import List

def split_words(text: str) -> List[str]:
    return re.findall(r'\b[\w\-]+\b', text)


print(split_words("Hello, Oleg Besedin! How are you?"))
