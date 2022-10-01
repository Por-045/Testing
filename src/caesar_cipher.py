def caesar_cipher(text, rotation):

    rotation = rotation % 26

    encrypt_text = ""

    for i in text:
        if ord(i) >= 97 and ord(i) <= (122-rotation):
            encrypt_text += chr(ord(i) + rotation)
        elif ord(i) > (122 - rotation) and ord(i) <= 122:
            encrypt_text += chr(ord(i) - 26 + rotation)
        elif ord(i) >= 65 and ord(i) <= (90-rotation):
            encrypt_text += chr(ord(i) + rotation)
        elif ord(i) > (90 - rotation) and ord(i) <= 90:
            encrypt_text += chr(ord(i) - 26 + rotation)
        else:
            encrypt_text+=i

    return encrypt_text
