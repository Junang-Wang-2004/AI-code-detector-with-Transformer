import collections

class C1:

    def generatePalindromes(self, a1):
        v1 = collections.Counter(a1)
        v2 = [char for v3 in v1 if v1[v3] % 2 == 1]
        if len(v2) > 1:
            return []
        v4 = v2[0] if v2 else ''
        v5 = {v3: v1[v3] // 2 for v3 in v1}
        v6 = sum(v5.values())
        v7 = []

        def build_path(a1):
            if len(a1) == v6:
                v1 = ''.join(a1)
                v7.append(v1 + v4 + v1[::-1])
                return
            for v2 in sorted(v5):
                if v5[v2] > 0:
                    v5[v2] -= 1
                    a1.append(v2)
                    build_path(a1)
                    a1.pop()
                    v5[v2] += 1
        build_path([])
        return v7
