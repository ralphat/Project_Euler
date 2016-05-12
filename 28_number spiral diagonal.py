t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    sum = 1
    m = (n+1)/2
    for q in range(2,m+1):
        sum = (sum + 4*(2*q-1)**2 - 6*m)%(10**9 + 7)
    print sum
