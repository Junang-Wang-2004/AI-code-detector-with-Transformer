class C1(object):

    def longestDiverseString(self, a1, a2, a3):
        """
        """
        v1 = [[a1, 'a'], [a2, 'b'], [a3, 'c']]
        v2 = []
        for v3 in range(a1 + a2 + a3):
            v1.sort(reverse=True)
            for v4, (v5, a3) in enumerate(v1):
                if v5 and v2[-2:] != [a3, a3]:
                    v2.append(a3)
                    v1[v4][0] -= 1
                    break
            else:
                break
        return ''.join(v2)
