def is_palindrome(text):
    # Convertimos a minúsculas y eliminamos caracteres que no son letras ni números
    text = text.lower()
    cleaned_text = ''.join(char for char in text if char.isalnum())
    
    # Por ahora devolvemos False porque todavía no comparamos
    return False

if __name__ == "__main__":
    while True:
        entrada = input("Ingrese una palabra o frase: ")
        if is_palindrome(entrada):
            print(f'"{entrada}" es un palíndromo')
        else:
            print(f'"{entrada}" no es un palíndromo')
