import random
import string

IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]


def permute(bits):
    permutation = ''
    for i in range(64):
        permutation += bits[IP[i] - 1]
    return permutation


def message_input():
    while True:
        msg = input('Message (8 char): ')
        if len(msg) == 8:
            return msg
        else:
            print('The message should have a length of 8. Try again.')


while True:
    try:
        print('Choose action:\n1. Manual input\n2. Random string\n3. Exit')
        opt = int(input('>'))
        if opt == 1 or opt == 2:
            message = ''
            if opt == 1:
                message = message_input()
            elif opt == 2:
                characters = string.ascii_letters + string.digits + string.punctuation
                message = ''.join(random.choice(characters) for i in range(8))
                print('Message: ', message)

            message = ''.join(format(ord(i), '08b') for i in message)
            print('\nMessage in binary format:\n', message, '\n')

            print('Initial permutation table:')
            for i in range(64):
                print(IP[i], ' ', end='')
                if ((i+1) % 8) == 0:
                    print()

            message = permute(message)
            print('\nMessage after initial permutation:\n', message, '\n')

            L1 = message[0:32]
            print('L1: ', L1, '\n')

        elif opt == 3:
            exit()
        else:
            print('\nInput is invalid.')

    except ValueError:
        print('\nInput is invalid.')
