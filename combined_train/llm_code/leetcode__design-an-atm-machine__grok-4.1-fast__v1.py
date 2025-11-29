class C1:

    def __init__(self):
        self.denominations = [20, 50, 100, 200, 500]
        self.available = [0] * 5

    def deposit(self, a1):
        for v1, v2 in enumerate(a1):
            self.available[v1] += v2

    def withdraw(self, a1):
        v1 = [0] * 5
        v2 = a1
        for v3 in range(4, -1, -1):
            v4 = self.denominations[v3]
            v5 = min(v2 // v4, self.available[v3])
            v1[v3] = v5
            v2 -= v5 * v4
        if v2 != 0:
            return [-1]
        for v3 in range(5):
            self.available[v3] -= v1[v3]
        return v1
