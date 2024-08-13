def recu(n):
    if n == 1:
        return 1
    else:
        return recu(n-1)+n

print(recu(5))

def tail_recu(n,result):
    if n == 0:
        return result
    else:
        return tail_recu(n-1,result+n)
print(tail_recu(5,0))

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(5))
for i in range(6):
    print(Fibonacci(i),end=",")

def for_loop_recursion(n):
    result = 0
    stack = []
    for i in range(n,0,-1):
        stack.append(i)
    while stack:
        result += stack.pop()
    return result
print(for_loop_recursion(5))