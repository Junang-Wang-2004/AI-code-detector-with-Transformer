from collections import Counter

class C1(object):

    def leastInterval(self, a1, a2):
        """
        """
        v1 = Counter(a1)
        v2, v3 = v1.most_common(1)[0]
        return max((v3 - 1) * (a2 + 1) + list(v1.values()).count(v3), len(a1))
