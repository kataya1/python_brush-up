

def fib(n):
    n_old = 0
    result = 1
    for i in range(n):
        n_new = result
        result = n_new + n_old
        n_old = n_new
    return result

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))