import re
from typing import List

def mask_numbers(text: str) -> str:
    return re.sub(r'\b\d+\.?\d*\b', '<num>', text)


print(mask_numbers("У него было 5 апельсина и 3.14 торта"))
