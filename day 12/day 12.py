import random
life = 0
number_list=[]
check_win=False
def check_number(user_input,selected_number):
    global life
    global check_win
    if (user_input==selected_number):
        print(f"Yes you guess the number correctly")
        check_win=True
    elif(user_input>selected_number):
        print(f"{user_input} is large ")
        life-=1
    else:
        print(f"{user_input} is smaller")
        life-=1

def main():
    global number_list
    global check_win
    for i in range(100):       # New List Is Being Created
        number_list.append(i+1)
    selected_number=random.choice(number_list)
    mode=input("Press 'e' for easy mofe and 'h' for hard mode ").lower()
    global life
    if mode=='e':
        life = 10
    else:
        life = 5
    while(life!=0 and check_win == False):
        print(f"You have {life} Lifes")
        user_number=int(input("Enter an number "))
        if user_number in number_list:
            check_number(user_number,selected_number)
        else:
            print("please enter the number between 1 to 100")
    if life==0:
        print("YOU LOSE BETTER LUCK NEXT TIME")
    
main()