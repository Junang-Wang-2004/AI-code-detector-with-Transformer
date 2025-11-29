class C1:

    def splitIntoFibonacci(self, a1):
        v1 = len(a1)
        v2 = (1 << 31) - 1

        def helper(a1, a2, a3, a4):
            if a1 == v1:
                return len(a4) >= 3
            v1 = a2 + a3
            if v1 > v2:
                return False
            v2 = str(v1)
            v3 = len(v2)
            if a1 + v3 > v1 or a1[a1:a1 + v3] != v2:
                return False
            a4.append(v1)
            if helper(a1 + v3, a3, v1, a4):
                return True
            a4.pop()
            return False
        for v3 in range(1, min(v1, 11)):
            if a1[0] == '0' and v3 > 1:
                continue
            v4 = int(a1[:v3])
            if v4 > v2:
                break
            for v5 in range(v3 + 1, min(v1 + 1, v3 + 11)):
                if a1[v3] == '0' and v5 - v3 > 1:
                    continue
                v6 = int(a1[v3:v5])
                if v6 > v2:
                    break
                v7 = [v4, v6]
                if helper(v5, v4, v6, v7):
                    return v7
        return []
