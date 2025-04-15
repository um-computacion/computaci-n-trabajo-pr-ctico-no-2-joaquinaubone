def is_palindrome(text):
    text = text.lower()
    cleaned_text = ''.join(char for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

if __name__ == "__main__":
    while True:
        entrada = input("Ingrese una palabra o frase: ")
        if is_palindrome(entrada):
            print(f'"{entrada}" es un palíndromo')
        else:
            print(f'"{entrada}" no es un palíndromo')
