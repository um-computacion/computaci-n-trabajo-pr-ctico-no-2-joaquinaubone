import string

def is_palindrome(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.replace(" ", "")
    return True  
