def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_pos = (ord(char) - start + shift) % 26
            char = chr(start + new_pos)
        result += char
    return result

print(caesar_cipher("Hello", 1))