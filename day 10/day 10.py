operation_list=["+","-","*","/"]
def add(first,second):
    return(first+second)
def sub(first,second):
    return(first-second)
def mul(first,second):
    return(first*second)
def div(first,second):
    return(first/second)

first_number=float(input("Enter the first nubmer: "))
for i in operation_list:
    print(i)

check_loop=True
while(check_loop):
    operation=input("pick an operation: ")
    ans=float(input("What's the next nubmer: "))
    print(f"Therefore {str(first_number)+operation+str(ans)} =",end=" ")
    index=operation_list.index(operation)
    if (index==0):
        ans=add(first_number,ans)
    elif(index==1):
        ans=sub(first_number,ans)
    elif(index==2):
        ans=mul(first_number,ans)
    elif(index==3):
        ans=div(first_number,ans)  
    print(ans)
    check_user=input("Press Y to continue and N to end the calculation ").lower()
    if(check_user=="y"):
        first_number=ans
    else:
        check_loop=False