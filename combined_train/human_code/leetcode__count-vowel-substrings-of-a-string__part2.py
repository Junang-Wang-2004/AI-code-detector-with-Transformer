import collections

class C1(object):

    def countVowelSubstrings(self, a1):
        """
        """
        v1 = set('aeiou')
        v2 = 5

        def atMostK(a1, a2):
            v1 = collections.Counter()
            v2 = v3 = 0
            for v4, v5 in enumerate(a1):
                if v5 not in v1:
                    v1 = collections.Counter()
                    v3 = v4 + 1
                    continue
                v1[v5] += 1
                while len(v1) > a2:
                    v1[a1[v3]] -= 1
                    if not v1[a1[v3]]:
                        del v1[a1[v3]]
                    v3 += 1
                v2 += v4 - v3 + 1
            return v2
        return atMostK(a1, v2) - atMostK(a1, v2 - 1)
