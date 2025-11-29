class C1:

    def fib(self, a1):
        if a1 <= 1:
            return a1
        v1, v2 = (1, 1)
        for v3 in range(3, a1 + 1):
            v1, v2 = (v2, v1 + v2)
        return v2
