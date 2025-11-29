class C1:

    def longestWord(self, a1):
        v1 = set(a1)
        v2 = sorted(a1, key=lambda w: (-len(w), w))
        for v3 in v2:
            if all((v3[:i + 1] in v1 for v4 in range(len(v3)))):
                return v3
        return ''
