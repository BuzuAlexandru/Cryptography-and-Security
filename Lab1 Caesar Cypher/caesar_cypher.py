def txt_input():
    while True:
        txt = input('Input the text you want to encrypt: ')
        txt.replace(' ', '')
        if txt.isalpha():
            return txt.upper()
        else:
            print('The text should only contain uppercase/lowercase letters of the English alphabet. Try again.')

def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


# check the above function
intercept_text = intercept()