import random

while True:
    try:
        low = int(input("please enter the low number;")) 
        high = int(input("please enter the high number;"))
        random_num = random.randint(low, high)
        break
    except:
        print("pleas enter a valid number:")
        

list = []
counter = 5


while True:
    
    try:
        guess = int(input(f" you have {counter} chance to guess,\n Enter your guess number;"))
        
        if guess == random_num:
            print('|---------------------|')
            print('|      you won :)     |')
            print('|---------------------|')
            break    
        elif guess > high:
            print("!!! its out of the range !!!")
        elif guess < low:
            print("!!! its out of the range !!!")
        elif guess > random_num:
            print('its too far, go down :)')
        else:
            print('its too far, go higher :)')
            
        counter -= 1
        list.append(guess)
        
        if counter == 0:
            print('|---------------------|')
            print('|    you lost :(      |')
            print('|  the number is:',random_num,' |')
            print('|---------------------|')
            break
    
    except:
        print("pleas enter a valid number")