a = int(input())
if (a % 4 == 0 and a % 100 != 0):
    print("Nam nhuan")
elif (a % 400 == 0):
    print("Nam nhuan")
else:
    print("K phai nam nhuan")
