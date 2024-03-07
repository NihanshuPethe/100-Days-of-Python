import random
import os
cards_value=[1,2,3,4,5,6,7,8,9,10,10,10,10]
yes_no=[0,1]
user_score=0
computer_score=0
user_cards=[]
computer_cards=[]
user_win=True
play_game=True
loop=True
computer_overvalue=False

def over_value(score):
    if(score>23):
        return True
    else:
        return False

def check_win(user_score,computer_score):
    if(user_score>23 and computer_score>23):
        print("Both lose")
    elif(user_score>23 or computer_score>23):
        if(user_score>23):
            print("User lose")
        else:
            print("User Win")
    elif(user_score>computer_score):
        print("User Win")
    else:
        print("User lose")

while(play_game):
    os.system('cls')
    print("LETS START THE GAME")
    user_cards.clear()
    computer_cards.clear()
    for i in range(2):
        user_cards.append(random.choice(cards_value))
        computer_cards.append(random.choice(cards_value))
    print(f"current user score = {sum(user_cards)}") 
    print(f"computer first card is {computer_cards[0]}")
    while(sum(computer_cards)<=17):
        computer_cards.append(random.choice(cards_value))
        computer_score=sum(computer_cards)
        computer_overvalue=over_value(computer_score)
    # print(computer_overvalue)
    if(computer_overvalue):
        loop=False
    else:
        loop=True
    while(loop):  
        temp=input("Preas 'y'to add the card and 'n'to skip ").lower()
        if( temp == 'y'):
            user_cards.append(random.choice(cards_value))
            print(f"current user score = {sum(user_cards)}")
            user_score=sum(user_cards)
            if(over_value(user_score)):
                print("over value")
                break
        elif(temp == 'n'):
            loop=False
            break;
    user_score=sum(user_cards)
    computer_score=sum(computer_cards)
    print(f"Your final score was {user_score} and Computer final score was {computer_score}")
    check_win(user_score,computer_score)
    play_again=input("Preas 'y'to play again and 'n'to stop ").lower()
    if play_again=="n":
        play_game=False
        break;