n = int(input())
sum = 0
for i in range(1,n+1):
    gt = 1
    for j in range(1,i+1):
        gt *= j
    sum += gt
print(sum)