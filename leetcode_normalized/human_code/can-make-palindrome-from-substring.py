import itertools

class C1(object):

    def canMakePaliQueries(self, a1, a2):
        """
        """
        v1 = 26
        v2, v3 = ([0] * v1, [[0] * v1])
        for v4 in a1:
            v2[ord(v4) - ord('a')] += 1
            v3.append(v2[:])
        return [sum(((b - a) % 2 for v5, v6 in zip(v3[left], v3[right + 1]))) // 2 <= k for v7, v8, v9 in a2]
