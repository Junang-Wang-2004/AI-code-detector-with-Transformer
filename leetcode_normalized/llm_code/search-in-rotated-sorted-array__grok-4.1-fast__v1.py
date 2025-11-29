class C1:

    def search(self, a1, a2):
        v1, v2 = (0, len(a1) - 1)
        while v1 <= v2:
            v3 = (v1 + v2) // 2
            if a1[v3] == a2:
                return v3
            if a1[v1] <= a1[v3]:
                if a2 >= a1[v1] and a2 < a1[v3]:
                    v2 = v3 - 1
                else:
                    v1 = v3 + 1
            elif a2 > a1[v3] and a2 <= a1[v2]:
                v1 = v3 + 1
            else:
                v2 = v3 - 1
        return -1
