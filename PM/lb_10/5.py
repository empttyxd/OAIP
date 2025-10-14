import re
from typing import List

def extract_tags(html: str) -> List[str]:
    return re.findall(r'<\/?([a-zA-Z0-9]+)(?:>|\/)', html)


print(extract_tags("<div><p>Hello</p><br/></div>"))
