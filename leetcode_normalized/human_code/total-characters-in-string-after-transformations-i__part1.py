v1 = 10 ** 9 + 7
v2 = 10 ** 5
v3 = [0] * (v2 + 26)
for v4 in range(26):
    v3[v4] = 1
for v4 in range(26, len(v3)):
    v3[v4] = (v3[v4 - 26] + v3[v4 - 26 + 1]) % v1

class C1(object):

    def lengthAfterTransformations(self, a1, a2):
        """
        """
        return reduce(lambda accu, x: (accu + x) % v1, (v3[ord(x) - ord('a') + a2] for v1 in a1), 0)
