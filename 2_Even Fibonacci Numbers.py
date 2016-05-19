t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    a = 1
    b = 2
    sum = 0
    while a<=n:
        if a%2==0:
            sum = sum+a
        b = a+b
        a = b-a
    print sum
