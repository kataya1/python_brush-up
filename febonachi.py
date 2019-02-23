import time
import pdb
# breakpoint()
def fib(n):
    n_old = 0
    result = 1
    for i in range(n):
        n_new = result
        result = n_new + n_old
        n_old = n_new
    return result

start1 = time.perf_counter_ns()
def printfib(n):
    for i in range(n):
        print(i+1, end=" ")
        # print("_",end="")
        print(fib(i))
end1 = time.perf_counter_ns()
#efficent fib
start2 = time.perf_counter_ns()
def print_fib_efficent(n):
    n_old = 0
    result = 1
    for i in range(n):
        print(result)
        n_new = result
        result = n_new + n_old
        n_old = n_new
end2 = time.process_time_ns()
printfib(1000)
print_fib_efficent(10000)
print(end1 - start1)
print(end2 - start2)
def fib_memoize(n):
    memo = [None] * (n+1)

# object oriented implementation of fib
# class fib(n):
#

