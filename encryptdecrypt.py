def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice.lower() == 'e':
        result = encrypt(message, shift)
        print(f"Encrypted message: {result}")
    elif choice.lower() == 'd':
        result = decrypt(message, shift)
        print(f"Decrypted message: {result}")
    else:
        print("Invalid choice! Please enter 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
