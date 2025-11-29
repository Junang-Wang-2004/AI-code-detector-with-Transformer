class C1(object):

    def clearStars(self, a1):
        """
        """
        v1 = list(a1)
        v2 = [[] for v3 in range(26)]
        for v4, v5 in enumerate(a1):
            if v5 != '*':
                v2[ord(v5) - ord('a')].append(v4)
                continue
            for v6 in v2:
                if not v6:
                    continue
                v1[v6.pop()] = '*'
                break
        return ''.join((v5 for v5 in v1 if v5 != '*'))
