from string import ascii_lowercase

class C1(object):

    def ladderLength(self, a1, a2, a3):
        """
        """
        v1 = set(a3)
        if a2 not in v1:
            return 0
        v2, v3 = ({a1}, {a2})
        v4 = 2
        while v2:
            v1 -= v2
            v5 = set()
            for v6 in v2:
                for v7 in (v6[:i] + c + v6[i + 1:] for v8 in range(len(a1)) for v9 in ascii_lowercase):
                    if v7 not in v1:
                        continue
                    if v7 in v3:
                        return v4
                    v5.add(v7)
            v2 = v5
            v4 += 1
            if len(v2) > len(v3):
                v2, v3 = (v3, v2)
        return 0
