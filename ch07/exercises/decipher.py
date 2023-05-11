def decipher(text, shift):
    """
    Encrypts or decrypts a message using the Caesar cipher technique.

    args:
        text:str = the message to encrypt or decrypt
        shift:int = the number of positions to shift each letter
    return:
        :str = the encrypted or decrypted message
    """

    result = ""
    for char in text:
        if char.isalpha():
            # Determine the case of the character
            start = ord('A') if char.isupper() else ord('a')
            # Calculate the new position of the character after the shift
            new_pos = (ord(char) - start + shift) % 26
            # Convert the new position back to a character
            char = chr(start + new_pos)
        result += char
    return result

def main():
    encrypted = open("encrypted-#B00789193.txt", "r")
    encrypted_msg = encrypted.read()
    
    # decrypting contents of the file and writing it in decrypted.txt
    decrypted_msg = decipher(encrypted_msg, 0)
    decrypted = open("decrypted.txt", "w")
    decrypted.write(decrypted_msg)

    # close files
    encrypted.close()
    decrypted.close()

main()