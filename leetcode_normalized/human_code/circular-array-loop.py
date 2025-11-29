class C1(object):

    def circularArrayLoop(self, a1):
        """
        """

        def next_index(a1, a2):
            return (a2 + a1[a2]) % len(a1)
        for v1 in range(len(a1)):
            if a1[v1] == 0:
                continue
            v2, v3 = (v1, v1)
            while a1[next_index(a1, v2)] * a1[v1] > 0 and a1[next_index(a1, v3)] * a1[v1] > 0 and (a1[next_index(a1, next_index(a1, v3))] * a1[v1] > 0):
                v2 = next_index(a1, v2)
                v3 = next_index(a1, next_index(a1, v3))
                if v2 == v3:
                    if v2 == next_index(a1, v2):
                        break
                    return True
            v2, v4 = (v1, a1[v1])
            while a1[v2] * v4 > 0:
                v5 = next_index(a1, v2)
                a1[v2] = 0
                v2 = v5
        return False
