import timing

code = "[x**3 for x in range(1000)]"

result = timing.timeit(code, 100)

print(result)