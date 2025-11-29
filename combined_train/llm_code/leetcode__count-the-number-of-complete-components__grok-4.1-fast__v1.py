class C1:

    def countCompleteComponents(self, a1, a2):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [False] * a1

        def check_component(a1):
            if v5[a1]:
                return False
            v1 = 0
            v2 = 0
            v3 = [a1]
            v5[a1] = True
            while v3:
                v4 = v3.pop()
                v1 += 1
                v2 += len(v1[v4])
                for v5 in v1[v4]:
                    if not v5[v5]:
                        v5[v5] = True
                        v3.append(v5)
            return v1 * (v1 - 1) == v2
        return sum((check_component(i) for v6 in range(a1) if not v5[v6]))
