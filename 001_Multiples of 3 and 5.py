t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    n = n-1
    l = n/3
    m = n/5
    o = n/15
    sum = (l*(l+1)*3 + m*(m+1)*5 - o*(o+1)*15)/2
    print sum
