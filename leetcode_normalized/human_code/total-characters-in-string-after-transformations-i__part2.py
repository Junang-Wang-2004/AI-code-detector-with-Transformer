class C1(object):

    def lengthAfterTransformations(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [1] * 26
        for v3 in range(26, ord(max(a1)) - ord('a') + a2 + 1):
            v2[v3 % 26] = (v2[(v3 - 26) % 26] + v2[(v3 - 26 + 1) % 26]) % v1
        return reduce(lambda accu, x: (accu + x) % v1, (v2[(ord(x) - ord('a') + a2) % 26] for v4 in a1), 0)
