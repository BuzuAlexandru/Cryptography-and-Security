alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
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
            print('The text should only contain letters of the Romanian alphabet. Try again.')


def key_input():
    while True:
        key = input('Secret key (7+ char): ')
        key = key.replace(' ', '').upper()
        temp_set = set(key)
        if temp_set.issubset(alpha_set) and len(key) >= 7:
            return key
        else:
            print('The key should only contain letters of the Romanian alphabet and have a length of at least 7. Try '
                  'again.')


def cypher(text, key):
    result = ''
    abc = alphabet

    for i, char in enumerate(text):
        result += abc[((abc.find(char) + key[i % len(key)]) % len(abc))]

    return result


def selection(action):
    text = txt_input(action)
    key = []

    for c in key_input():
        key.append(alphabet.find(c))

    if action == 1:
        print('The encrypted text is: ', end='')
    elif action == 2:
        for i in range(len(key)):
            key[i] = -1 * key[i]
        print('The decrypted text is: ', end='')

    print(cypher(text, key))


while True:
    try:
        print('Choose action:\n1. Encrypt\n2. Decrypt\n3. Exit')
        opt = int(input('>'))
        if opt == 1 or opt == 2:
            selection(opt)

        elif opt == 3:
            exit()
        else:
            print('\nInput is invalid.')

    except ValueError:
        print('\nInput is invalid. Try again')
