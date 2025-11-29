class C1(object):

    def maxSubsequence(self, a1, a2):
        v1 = sorted(enumerate(a1), key=lambda pair: pair[1], reverse=True)[:a2]
        v2 = sorted(v1)
        return [value for v3, v4 in v2]
