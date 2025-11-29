class C1:

    def longestSubsequenceRepeatedK(self, a1, a2):
        v1 = {}
        for v2 in a1:
            v1[v2] = v1.get(v2, 0) + 1
        v3 = []

        def feasible(a1, a2, a3):
            if not a1:
                return True
            v1 = 0
            v2 = 0
            for v3 in a2:
                if v3 == a1[v1]:
                    v1 += 1
                    if v1 == len(a1):
                        v2 += 1
                        v1 = 0
                        if v2 == a3:
                            return True
            return False

        def explore(a1, a2):
            if not feasible(a1, a1, a2):
                return
            if len(a1) > len(v3):
                v3[:] = a1[:]
            for v1 in range(ord('z'), ord('a') - 1, -1):
                v2 = chr(v1)
                if a2.get(v2, 0) >= a2:
                    a2[v2] = a2.get(v2, 0) - a2
                    a1.append(v2)
                    explore(a1, a2)
                    a1.pop()
                    a2[v2] += a2
        explore([], v1)
        return ''.join(v3)
