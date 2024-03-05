char_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def dencode(user_str,shift,option_selected):
    new_str=""
    for i in user_str:
        if i==" ":
            new_str+=" "
            continue
        elif i=='1' or i=='2'or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0':
            new_str+=i
        else :
            index=char_list.index(i)
            if option_selected==1:
                new_index=(index+shift)%26
            else:
                new_index=(index-shift)%26
            new_str += char_list[new_index]
    return new_str

bool_a=True
while bool_a:
    option_selected=int(input("Press 1 to Encode\nPress 2 to Decode \n"))
    user_str=input("Enter a string ").lower()
    shift=int(input("Enter the shift n.o "))
    new_str=""
    if option_selected == 1 or option_selected==2:
        new_str=dencode(user_str,shift,option_selected)
    else:
        print("Input Error")
    print(new_str)
    check_exit=int(input("Press 1 to continue and 2 to exit "))
    if check_exit==2:
        bool_a=False