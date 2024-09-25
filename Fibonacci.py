# Fibonacci sequence
# 0,1,1,2,3,5,8,13,21
# 0 1 20
# [0,1,1]
def fib(n):
    l = [0,1]
    for i in range(2,n):
        last = l[-1]
        b_last = l[-2]
        v = last + b_last
        l.append(v)
    print(l)

def fib_while(n):
    l = [0,1] 
    counter = 2
    while counter < n:
        last = l[-1]
        b_last = l[-2]
        v = last + b_last
        l.append(v)
        counter += 1
    print(l)

fib_while(8)