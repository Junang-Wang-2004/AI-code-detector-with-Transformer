class C1(object):

    def sortVowels(self, a1):
        """
        """

        def inplace_counting_sort(a1, a2=False):
            if not a1:
                return
            v1 = [0] * (max(a1) + 1)
            for v2 in a1:
                v1[v2] += 1
            for v3 in range(1, len(v1)):
                v1[v3] += v1[v3 - 1]
            for v3 in reversed(range(len(a1))):
                while a1[v3] >= 0:
                    v1[a1[v3]] -= 1
                    v4 = v1[a1[v3]]
                    a1[v3], a1[v4] = (a1[v4], ~a1[v3])
            for v3 in range(len(a1)):
                a1[v3] = ~a1[v3]
            if a2:
                a1.reverse()
        v1 = 'AEIOUaeiou'
        v2 = {x: i for v3, v4 in enumerate(v1)}
        v5 = [v2[v4] for v4 in a1 if v4 in v2]
        inplace_counting_sort(v5, reverse=True)
        return ''.join((v1[v5.pop()] if v4 in v2 else v4 for v4 in a1))
