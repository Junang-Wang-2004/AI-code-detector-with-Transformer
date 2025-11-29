import collections

class C1(object):

    def countVowelSubstrings(self, a1):
        """
        """
        v1 = set('aeiou')
        v2 = 5

        def atLeastK(a1, a2):
            v1 = collections.Counter()
            v2 = v3 = v4 = 0
            for v5, v6 in enumerate(a1):
                if v6 not in v1:
                    v1 = collections.Counter()
                    v3 = v4 = v5 + 1
                    continue
                v1[v6] += 1
                while len(v1) > a2 - 1:
                    v1[a1[v4]] -= 1
                    if not v1[a1[v4]]:
                        del v1[a1[v4]]
                    v4 += 1
                v2 += v4 - v3
            return v2
        return atLeastK(a1, v2)
