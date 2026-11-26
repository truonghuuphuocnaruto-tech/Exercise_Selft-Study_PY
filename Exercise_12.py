# tỉnh tổng s(x,n) = x + (x^2/2!) + .. + (x^n/n!)
x = int(input())
n = int(input())
sum = 0
for i in range(1,n+1):
    gt = 1
    for j in range(1,i+1):
        gt *= j
    sum += (x**i / gt)
print(round(sum,2))