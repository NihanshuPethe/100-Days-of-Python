import random
bool_1=True

while bool_1:

    ITEM=["Rock","Paper","Scissor"]
    Index=[0,1,2]
    print("What do you choose? Type 0 for Rock, 1 for Paper , 2 for Scissor")
    User_choice=int(input())
    Cpu_choice= random.choice(Index)
    # print(Cpu_choice)
    print(f"You have Selected {ITEM[User_choice]}")
    print(f"CPU have Selected {ITEM[Cpu_choice]}")
    # check will condition
    if User_choice==Cpu_choice:
        print("Draw")
    else:
        if (User_choice== 0):
            if(Cpu_choice == 1):
                print('Computer Wins')
            else:
                # user wins
                print ("You Win ")
        
        if (User_choice== 1):
            if(Cpu_choice == 2):
                print('Computer Wins')
            else:
                # user wins
                print ("You Win ")
        
        if (User_choice== 2):
            if(Cpu_choice == 0):
                print('Computer Wins')
            else:
                # user wins
                print ("You Win ")
    play_again= int(input("Press 1 to Quit "))
    if play_again == 1:
        bool_1=False
        break
print("exit")  
        
        