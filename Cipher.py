
from time import sleep



## Welcome Text 
welcomeText=['Hello Welcome to encrypt and decrypt script By Nazbeen-Ai',
            'first of all Read this Text to understanding how caeser Cipher Work',
            'The number of spaces you shift your letters (between 1 and 26) is the key in the Caesar cipher. Unless you know the key (the number used to encrypt the message), you won’t be able to decrypt the secret code. The example in Figure 14-2 shows the letter translations for the key 3'
            ]

for R in welcomeText:
    sleep(1)
    print(R)

print('I hope you understand How Ceasar Cipher Work \n')



SYMBOLS= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE=len(SYMBOLS)




def getMode():
    while True:
        print('Do you wish  to encrypt od decrypt a message? ')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd' ]:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d". ')


def getMessage():
    print('Enter your message: ')
    return input()

def getKey():
    Key = 0
    while True:
        print("Enter the Key number (1-%s)" %(MAX_KEY_SIZE))
        key=int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessae(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex= SYMBOLS.find(symbol)
        if symbolIndex == -1:
            translated += symbol
        else:
            symbolIndex += key
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -=len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]

    return translated


mode= getMode()
message = getMessage()
key = getKey()
print('Your translated text is :')
print(getTranslatedMessae(mode, message, key))