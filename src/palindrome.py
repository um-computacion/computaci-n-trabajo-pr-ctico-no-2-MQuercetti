import re  

def is_palindrome(Text):
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', Text).lower()
    return cleaned_text == cleaned_text[::-1]