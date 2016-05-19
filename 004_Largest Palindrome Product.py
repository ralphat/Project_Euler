import math
def check(i):
    for j in range(int(math.sqrt(i)),100,-1):
        if(i%j==0):
            if(i/j<1000):
                return 1
def pal(n):
    for i in range(n-1,101100,-1):
        if(str(i)==str(i)[::-1]):
            if(check(i)):
                return i
t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    print pal(n)
