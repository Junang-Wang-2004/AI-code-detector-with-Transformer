class C1(object):

    def countOfSubstrings(self, a1, a2):
        """
        """
        v1 = set('aeiou')

        def count(a1):

            def update(a1, a2):
                if a1[a1] not in v1:
                    curr2[0] += a2
                    return
                v1 = ord(a1[a1]) - ord('a')
                if cnt[v1] == 0:
                    curr1[0] += 1
                cnt[v1] += a2
                if cnt[v1] == 0:
                    curr1[0] -= 1
            v1 = 0
            v2 = [0] * 26
            v3, v4 = ([0], [0])
            v5 = 0
            for v6 in range(len(a1)):
                update(v6, +1)
                while v3[0] == len(v1) and v4[0] >= a1:
                    v1 += len(a1) - v6
                    update(v5, -1)
                    v5 += 1
            return v1
        return count(a2) - count(a2 + 1)
