import string


alphabet = string.ascii_uppercase
alpha_set = set(alphabet)


def txt_input(action):
    if action == 1:
        operation = 'encrypt'
    else:
        operation = 'decrypt'

    while True:
        txt = input(f'Input the text you want to {operation}: ')
        txt = txt.replace(' ', '').upper()

        temp_set = set(txt)
        if temp_set.issubset(alpha_set):
            return txt
        else:
            print('The text should only contain letters of the English alphabet. Try again.')


def key1_input():
    while True:
        try:
            key = int(input('Secret key (1-26): '))
            if key < 1 or key > 26:
                print('The key should be an integer number between 1 and 26 . Try again.')
            else:
                return key
        except ValueError:
            print('The key should be an integer number between 1 and 26 . Try again.')


def key2_input():
    while True:
        key = input('Second secret key: ')
        key = key.upper()
        temp_set = set(key)
        if temp_set.issubset(alpha_set) and len(key) >= 7:
            return key
        else:
            print('The key should only contain letters of the English alphabet and have a length of at least 7. Try '
                  'again.')


def cypher(text, abc, key):
    result = ''

    for char in text:
        result += abc[((abc.find(char) + key) % 26)]

    return result


def selection(action, abc, keys):
    text = txt_input(action)
    key1 = key1_input()
    if keys == 2:
        key2 = key2_input()
        abc = ''.join(dict.fromkeys(key2 + abc))
        print('Modified alphabet is: ', abc)

    if action == 1:
        print('The encrypted text is: ', cypher(text, abc, key1))
    elif action == 2:
        print('The decrypted text is: ', cypher(text, abc, -1 * key1))


while True:
    try:
        print('Choose action:\n1. Encrypt\n2. Decrypt\n3. Exit')
        opt = int(input('>'))
        if opt == 1 or opt == 2:
            print('\nType:\n1. One key\n2. Two keys')
            t = int(input('>'))

            while t != 1 and t != 2:
                print('\nInput is invalid.')
                print('\nType:\n1. One key\n2. Two keys')
                t = int(input('>'))

            selection(opt, alphabet, t)

        elif opt == 3:
            exit()
        else:
            print('\nInput is invalid.')

    except ValueError:
        print('\nInput is invalid. Try again')
