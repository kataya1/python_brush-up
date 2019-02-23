def fib(n):
    n_old = 0
    result = 1
    for i in range(n):
        n_new = result
        result = n_new + n_old
        n_old = n_new
    return result


def printfib(n):
    for i in range(n):
        print(i+1, end=" ")
        # print("_",end="")
        print(fib(i))

#efficent fib
def print_fib_efficent(n):
    n_old = 0
    result = 1
    for i in range(n):
        print(result)
        n_new = result
        result = n_new + n_old
        n_old = n_new

printfib(9)
print_fib_efficent(9)
# # efficent implementation of fib
# class fib(n):
#