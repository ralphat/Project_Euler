t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    h = m = n
    while n%2==0:
        n = n/2
        h = 2
    i = 3
    while i<=int(m**0.5):
        while n%i==0:
            n = n/i
            h = i
        i = i+2
    if n>h:
        h = n
    print h
