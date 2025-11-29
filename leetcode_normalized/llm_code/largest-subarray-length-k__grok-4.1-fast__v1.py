class C1(object):

    def largestSubarray(self, a1, a2):
        v1 = len(a1)
        v2 = a2 - 1
        v3 = 1
        v4 = v1 - a2 + 1
        while v3 < v4:
            v5 = v2 - a2 + 1
            v6 = 0
            while v6 < a2 and a1[v5 + v6] == a1[v3 + v6]:
                v6 += 1
            if v6 < a2 and a1[v5 + v6] >= a1[v3 + v6]:
                v3 += v6 + 1
            else:
                v2 = v3 + a2 - 1
                v3 += v6 + 1
        return a1[v2 - a2 + 1:v2 + 1]
