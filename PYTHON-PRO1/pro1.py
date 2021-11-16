import random
number = random.randint(1, 9)
print(number)
chances = 0

while chances < 5 :
        enter = int(input("Guess a number between 1-9 "))
        if enter != number :
            # if number entered by user is same as the generated number by randint function
            print("Oh no! You got it wrong! Want a hint? try something greater or lower?")
            # then break from loop using loop
            # control statements "break"
        elif enter == number :
            print("Congratulation You Won!!!")
        # check wether the user guessed the correct number
        else :
            print("YOU LOSE!! The number was", number)
        break
    chances = chances+1