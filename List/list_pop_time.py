import timeit
from timeit import Timer

pop_zero = Timer("x.pop(0)","from __main__ import x")
pop_end = Timer("x.pop()","from __main__ import x")

x = list(range(2000000))

print("Time: ",pop_zero.timeit(number=1000))

x = list(range(2000000))
print("Time: ",pop_end.timeit(number=1000))