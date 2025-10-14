import re
from typing import List

def find_repeated_words(text: str) -> List[str]:
    match = re.findall(r'\b(\w+)\s+\1\b', text)
    return list(dict.fromkeys(match))


print(find_repeated_words("why we still here?"))
