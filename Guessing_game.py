# This game is for you to pick/guess the random Item from the list & you have 6 attempt 
# after pick the element wrong the attampt will be decreased 
# and if you guess correctly the element of the list will eleminate 1

import random

def gussing_game():
    Item_list = ['pizza', 'bananas', 'coke']
    attempt = 6
    print(f"you have {attempt} attempts")
    while attempt > 0:
        print (Item_list)
        pick = random.choice(Item_list)
        player = input("\nOne element you choose: ")
        if player == pick:
            print("You guessed the words correctly!")
            Item_list.remove(pick)
        else:
            attempt = attempt - 1
            print(f"{attempt} attempt(s) left")
        
        if attempt == 0 or len(Item_list) == 0:
            Ask = input("\nDo you want to play again? (y/n)  : ")
            if Ask == 'y':
                gussing_game()
            else:
                print("Thank you !")
                break
gussing_game()