import sympy
v1 = int(input())
print(len(list(filter(lambda x: len(sympy.divisors(x)) == 8, range(1, v1 + 1, 2)))))
