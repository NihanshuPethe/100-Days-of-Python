from data_14 import data 
import random
import os
Ans='a'
def generate_person():
    person=random.choice(data)
    return person
def print_detail(person):
    name=person["name"]
    description=person["description"]
    country=person["country"]
    return f"\n\n Name: {name} \n description: {description} country: {country}"
def check(person_a,person_b,user_guess):
    global Ans
    if(person_a["follower_count"]>person_b["follower_count"] and user_guess=='a'):
        Ans ='a'
        return True
    elif(person_b["follower_count"]>person_a["follower_count"] and user_guess=='b'):
        Ans ='b'
        return True
    else:
        return False
def game():

    play_game=True
    score=0
    global Ans
    person_a=generate_person()
    print("Welcome")
    while play_game:
        os.system('cls')
        print(f"Current Score is {score}")
        person_b=generate_person()
        while(person_a==person_b):
            person_b=generate_person()
        print(f"Detain of person A {print_detail(person_a)}")
        print("vs")
        print(f"Detain of person B {print_detail(person_b)}")
        user_guess=input("Enter the Option 'a' or 'b'").lower()
        ans = check(person_a,person_b,user_guess)
        if ans:
            if Ans =='b':
                person_a=person_b
            score+=1
        else:
            play_game=False
            print(f"Your guess was wrong \n Your Score is {score}")
            

game()