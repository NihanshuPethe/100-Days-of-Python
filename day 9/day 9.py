import os

record={}
name=[]
amount=[]
check_end=True
while(check_end):
    User_name=input("What is your name ")
    name.append(User_name)
    User_amount=int(input("What is your amount "))
    amount.append(User_amount)
    loop_check=input("Is there any other person press 'yes' or 'no' ").lower()
    if (loop_check=="no"):
        check_end=False
    os.system('cls')

for i,j in zip(name,amount):
    record.update({i:j})
large=0
for i in record:
    if record[i]>large:
        large=record[i]
        winner=i
print(f"And the winner is {winner}")
print(record)


