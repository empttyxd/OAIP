import re
from typing import List

def extract_dates(text: str) -> List[str]:
    pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return re.findall(pattern, text)


print(extract_dates("Встреча 15-01-2022 и  15/06/2025"))
