import collections

class C1:

    def rootCount(self, a1, a2, a3):
        v1 = collections.defaultdict(list)
        for v2, v3 in a1:
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4 = {(a, b) for v5, v6 in a2}

        def calc_down(a1, a2):
            v1 = 1 if (a1, a2) in v4 else 0
            for v2 in v1[a2]:
                if v2 != a1:
                    v1 += calc_down(a2, v2)
            return v1
        v7 = calc_down(-1, 0)
        v8 = 0

        def reorient(a1, a2, a3):
            nonlocal count
            a3 -= 1 if (a1, a2) in v4 else 0
            a3 += 1 if (a2, a1) in v4 else 0
            if a3 >= a3:
                v2 += 1
            for v3 in v1[a2]:
                if v3 != a1:
                    reorient(a2, v3, a3)
        reorient(-1, 0, v7)
        return v8
