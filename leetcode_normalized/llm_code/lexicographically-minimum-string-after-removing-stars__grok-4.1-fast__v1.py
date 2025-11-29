class C1:

    def clearStars(self, a1: str) -> str:
        v1 = [[] for v2 in range(26)]
        for v3, v4 in enumerate(a1):
            if v4 == '*':
                for v5 in v1:
                    if v5:
                        v5.pop()
                        break
            else:
                v1[ord(v4) - ord('a')].append(v3)
        v6 = []
        for v5 in v1:
            v6.extend(v5)
        v6.sort()
        return ''.join((a1[p] for v7 in v6))
