# viết chương trình người dùng nhập vào 1 số
# và kiểm tra xem số đó có phải là số ng/to hayk
n = int(input("Enter number: "))
check = True
while (check):
    check_ngto = True
    for i in range(2,n):
        if (n == 2):
            print("Yes")
        if (n > 2):
            if (n % i == 0):
                check_ngto = False; break
    if (check_ngto == False):
        print("No")
    else:
        print("YEa")
    print("Enter (continue or exit)")
    check_user = str(input())
    if (check_user == "continue"):
        n = int(input("Enter number: "))
        continue
    elif (check_user == "exit"):
        break
    else:
        print("Please enter (continue or exit)")
        while(True):
            check_user = str(input())
            if (check_user == "continue"):
                n = int(input("Enter number: "))
                break
            elif (check_user == "exit"):
                break
            else:
                print("Please enter (continue or exit)")
                continue
            
        