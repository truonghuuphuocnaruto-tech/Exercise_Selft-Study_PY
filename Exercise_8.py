import math 
a,b,c = map(float,(input()).split(' '))
delta = b**2 - 4 * a * c
x1 = - b + math.sqrt(abs(delta))
x2 = - b - math.sqrt(abs(delta))
if (a == 0 and b == 0 and c == 0):
    print("Phuong trinh co vo so nghiem")
elif (a == 0 and b == 0 and c != 0):
    print("Phuong trinh vo nghiem")
elif (a == 0 and b != 0):
    print("Phuong trinh co 1 nghiem duy nhat x =",-c/b)
elif (a != 0):
    if (delta > 0):
        print("x1 = ",x1," x2 =",x2)
    elif (delta == 0):
        print("x1 = x2 =",-b/(2*a))
    else:
        print("phuong trinh vo nghiem")