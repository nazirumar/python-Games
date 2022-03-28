from time import sleep
import random


def operatorsLists():
    operatorsList = ['1. addition', '2. Subtraction', '4. introductions']
    for i in operatorsList:
        print(i)
    opeartors = int(input('Select Operators Number :'))
   
def intro():
    print('Calculator games are a motivating and low stress way to help students learn about numbers and number facts')
    sleep(2)
    print('Are you Ready To play The Game ? ')
    sleep(2)
    print('Game start in two second ')

def add():
    Number1 =random.randint(1, 20)
    Number2 =random.randint(1, 20)
    print('\n What is ' + str(Number1) +   ' + ' + str(Number2) + ' ? ')
    try:
        while True:
            answer =int(input('Answer :  '))
            if answer == Number1 + Number2:
                print('Correct')
            elif (answer == 'E'):
                break
            else:
                print('Nope ! The answer is ' + str(Number1 - Number2))
    except ValueError:
        print("a and b must both be integers")

def sub(self):
    Number1 =random.randint(1, 20)
    Number2 =random.randint(1, 20)
    print('\n What is ' + str(Number1) +   ' - ' + str(Number2) + ' ? ')

    try: 

        print( ' If You want exit Enter E')
        answer =int(input('Answer :  '))
        if answer == Number1 - Number2:
            print('Correct')
        elif answer == 'E' or 'e':
            operatorsLists()
        
                
        else:
            print('Nope ! The answer is ' + str(Number1 - Number2))
    except ValueError:
        print("a and b must both be integers")
def divide ():
    Number1 =random.randint(1, 20)
    Number2 =random.randint(1, 20)
    print('\n What is ' + str(Number1) +   ' - ' + str(Number2) + ' ? ')

    try: 
        answer =int(input('Answer :  '))
        if answer == Number1 - Number2:
            print('Correct')
        else:
            print('Nope ! The answer is ' + str(Number1 - Number2))
    except ValueError:
        print("a and b must both be integers")
   
operatorsLists()
while True:
    add()
    
    # if opeartors == 1:  
    #     while True:
    #         Cal.add()
    # elif opeartors == 2:
    #     Cal.sub()
    # elif opeartors == 4:
    #     Cal.intro()
        
   