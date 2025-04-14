def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    while True:
        entrada = input("Ingrese una palabra o frase: ")
        if is_palindrome(entrada):
            print(f'"{entrada}" es un palíndromo\n')
        else:
            print(f'"{entrada}" no es un palíndromo\n')
