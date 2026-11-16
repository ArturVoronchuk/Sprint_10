import re

def normalize_address(addr: str) -> str:
    return addr.replace("улица", "").strip()

def extract_number(text):
    match = re.search(r"\d+", text)
    return int(match.group()) if match else None