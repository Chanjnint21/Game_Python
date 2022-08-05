
import random

def method1():

    pick = random.randint(1,10) # randint() method returns an integer number selected element from the specified range
    attempt = 5
    while attempt > 0:
        player = int(input("\nOne element you choose: "))
        if player < pick:
            attempt = attempt - 1
            print("the value is Greater")

        elif player > pick:
            print("the value id less")
            attempt = attempt - 1
            print(f"{attempt} attempt(s) left")

        else:
            print("you win")
            ask = input("Do you want to play again ?")

        if attempt == 0:
            print("The correct answer is", pick)
            print("You lose !!!")
            ask = input("\n Do you want to play again ?(y/n) :")
    if ask == "y" :
        method1()
    if ask == "n" :
        print("Thank you ... !")
method1()

def method2():
    inp = int(input("Enter the number: "))
    Item_list = []
    for i in range (1, inp+1):
        Item_list.append(int(i))
    attempt = 5
    print("you have",attempt ,"attempts")
    print (Item_list)
    while attempt > 0:
        pick = random.choice(Item_list)
        player = int(input("\nOne element you choose: "))
        
        if player < pick:
            attempt = attempt - 1
            print("the value is Greater")
            print(attempt,"attempt(s) left")

        elif player > pick:
            attempt = attempt - 1
            print("the value is less")
            print(attempt,"attempt(s) left")

        else:
            print("you win !!!!")
            ask = input("Do you want to play again ?")

        if attempt == 0:
            print("You lose !!!")
            ask = input("Do you want to play again ?")
    if ask == "y" :
        method2()
    if ask == "n" :
        print("Thank you ... !")
#method2()
