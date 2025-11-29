class C1(object):

    def sortArray(self, a1):
        v1 = len(a1)

        def get_cost(a1):
            v1 = [False] * v1
            v2 = 0
            v3 = 0
            for v4 in range(v1):
                if v1[v4]:
                    continue
                v5 = 0
                v6 = v4
                while not v1[v6]:
                    v1[v6] = True
                    v6 = (a1[v6] - a1) % v1
                    v5 += 1
                v2 += 1
                if v5 >= 2:
                    v3 += 1
            v7 = v1 - v2 + 2 * v3
            v8 = a1 * (v1 - 1) % v1
            if a1[v8] != 0:
                v7 -= 2
            return v7
        return min(get_cost(0), get_cost(1))
