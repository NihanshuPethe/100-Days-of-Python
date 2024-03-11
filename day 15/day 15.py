MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
Water=300
Milk=200
Coffee=100
Money=0
def Print_Report():
    '''Just print the report'''
    global Water
    global Milk
    global Coffee
    global Money
    print(f"Water = {Water}")
    print(f"Milk = {Milk}")
    print(f"Coffee = {Coffee}")
    print(f"Money = {Money}")

def is_possible(procuct):
    '''Check weather it is possible to make an coffee or not and return true of false'''
    global Water
    global Milk
    global Coffee
    global Money
    if(procuct=="espresso"):
        if(Water>=MENU[procuct]["ingredients"]["water"] and Coffee>=MENU[procuct]["ingredients"]["coffee"] ):
            return True
        else:
            return False
    elif(procuct=="latte"):
        if(Water>=MENU[procuct]["ingredients"]["water"] and Milk>=MENU[procuct]["ingredients"]["milk"] and Coffee>=MENU[procuct]["ingredients"]["coffee"] ):
            return True
        else:
            return False
    elif(procuct=="cappuccino"):
        if(Water>=MENU[procuct]["ingredients"]["water"] and Milk>=MENU[procuct]["ingredients"]["milk"] and Coffee>=MENU[procuct]["ingredients"]["coffee"] ):
            return True
        else:
            return False

def should_give_coffee(overall_money,user_input):
    '''It check weather the user user should get a coffee or not '''
    global Water
    global Milk
    global Coffee
    global Money
    if(user_input=="espresso" and overall_money>=MENU[user_input]["cost"]):
        print(f"Here is your {user_input}")
        Water=Water-MENU[user_input]["ingredients"]["water"]
        Coffee=Coffee-MENU[user_input]["ingredients"]["coffee"]
        cost= overall_money-MENU[user_input]["cost"]
        Money+=MENU[user_input]["cost"]
        print(f"Your change {cost}")
    elif(user_input=="latte" and overall_money>=MENU[user_input]["cost"]):
        print(f"Here is your {user_input}")
        Water=Water-MENU[user_input]["ingredients"]["water"]
        Milk=Milk-MENU[user_input]["ingredients"]["milk"]
        Coffee=Coffee-MENU[user_input]["ingredients"]["coffee"]
        cost=overall_money-MENU[user_input]["cost"]
        Money+=MENU[user_input]["cost"]
        print(f"Your change {cost}")
    elif(user_input=="cappuccino" and overall_money>=MENU[user_input]["cost"]):
        print(f"Here is your {user_input}")
        Water=Water-MENU[user_input]["ingredients"]["water"]
        Milk=Milk-MENU[user_input]["ingredients"]["milk"]
        Coffee=Coffee-MENU[user_input]["ingredients"]["coffee"]
        cost=overall_money-MENU[user_input]["cost"]
        Money+=MENU[user_input]["cost"]
        print(f"Your change {cost}")
    else:
        print(f"Not enough money for your {user_input}")

def count_coin(user_input):
    '''Take the money from the user and calculate the overall money and call the function should_give_coffee'''
    penny=int(input("How many penny : "))
    dime=int(input("How many dime : "))
    nickel=int(input("How many nickle : "))
    quatter=int(input("How many quatter : ")) 
    overall_money = penny*0.01+dime*0.10+ nickel*0.05 + quatter*0.25
    print(f"Over all money paid by you {overall_money}")
    should_give_coffee(overall_money,user_input) 

def main():
    '''main function'''
    while(True):
        user_input=input("What Would you like ? (espresso/latte/cappuccino) ").lower()
        if(user_input=="report"):
            Print_Report()
        elif(user_input=="off"):
            break
        else:
            check_is_possible = is_possible(user_input)
            if check_is_possible:
                count_coin(user_input)
            else:
                print("Sorry Unable to make coffee")
           
main()