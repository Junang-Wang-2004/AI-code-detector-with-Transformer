class C1(object):

    def removeSubstring(self, a1, a2):
        """
        """

        def count(a1):
            if a1 == '(':
                if cnt[0] < a2:
                    cnt[0] += 1
                elif cnt[0] > a2:
                    cnt[0] = 1
            elif cnt[0] >= a2:
                cnt[0] += 1
            else:
                cnt[0] = 0
        v1 = []
        v2 = [0]
        for v3 in a1:
            v1.append(v3)
            count(v3)
            if v2[0] != 2 * a2:
                continue
            for v4 in range(2 * a2):
                v1.pop()
            v2[0] = 0
            for v5 in range(max(len(v1) - (2 * a2 - 1), 0), len(v1)):
                count(v1[v5])
        return ''.join(v1)
