from memory_profiler import profile

@profile
def some_function():
    a = 13
    for i in range(5):
        a = a*a
    print(a)

some_function()
