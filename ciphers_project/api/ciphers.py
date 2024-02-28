


def caeser_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        if c.isupper():  # check if it's an uppercase character
            c_encoded = ((ord(c) - ord('A') + shift) % 26) + ord('A')
        elif c.islower():  # check if it's a lowercase character
            c_encoded = ((ord(c) - ord('a') + shift) % 26) + ord('a')
        else:
            c_encoded = ord(c)  # non-alphabet characters are not encoded
        cipher_text += chr(c_encoded)
    return cipher_text