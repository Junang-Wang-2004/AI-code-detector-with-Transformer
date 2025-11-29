class C1:

    def find132pattern(self, a1):
        v1 = len(a1)
        v2 = []
        v3 = float('-inf')
        for v4 in range(v1 - 1, -1, -1):
            if a1[v4] < v3:
                return True
            while v2 and a1[v2[-1]] < a1[v4]:
                v3 = a1[v2.pop()]
            v2.append(v4)
        return False
