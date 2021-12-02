
import re

def is_palindrome(string):
    str_lower = string.lower()
    palindrome=re.sub(r'[^a-z0-9\n\.]','',str_lower)
    print(palindrome)
    if len(palindrome) == 0:
        return False
    elif  palindrome== palindrome[::-1]:
        return True
    else:
        return False

