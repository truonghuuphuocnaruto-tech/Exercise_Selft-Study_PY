# viết chương trình in ra các số hoàn hảo từ 1 -> 1000
# số hoàn hoả là số có tổng các ước của nó bằng chính nó (không tính chính nó)
# vd: 6 = 1 + 2 + 3 = 6 => 6 là số hoàn hảo
for i in range(1,1000):
    check = 0
    if (i >= 4):
        for j in range(1,i):
            if (i % j == 0):
                check += j
    if (check == i):
        print(i, end = " ")