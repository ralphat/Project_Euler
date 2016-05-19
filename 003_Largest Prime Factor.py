t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    h = m = n
    while n%2==0:
        n = n/2
        h = 2
    i = 3
    while i<m:
        while n%i==0:
            n = n/i
            h = i
        i = i+2
    print h
