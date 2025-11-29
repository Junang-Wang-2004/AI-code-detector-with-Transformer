class C1:

    def sortVowels(self, a1: str) -> str:
        v1 = set('aeiouAEIOU')
        v2 = [ch for v3 in a1 if v3 in v1]
        v2.sort()
        v4 = []
        v5 = 0
        for v3 in a1:
            if v3 in v1:
                v4.append(v2[v5])
                v5 += 1
            else:
                v4.append(v3)
        return ''.join(v4)
