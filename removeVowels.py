import re

def anti_vowel(s):
    result = re.sub(r'[AEIOU]', '', s, flags=re.IGNORECASE)
    return result

print anti_vowel("johan")