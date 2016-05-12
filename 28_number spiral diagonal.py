# Python 2
t = int(raw_input())
d = 10**9 + 7
for i in range(t):
    n = int(raw_input())
    m = (n+1)/2
    sum = (16*(m**3) - 18*(m**2) + 14*m - 12 + 3)/3
    print (sum)%d
