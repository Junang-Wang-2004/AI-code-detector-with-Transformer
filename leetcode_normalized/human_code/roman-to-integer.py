class C1(object):

    def romanToInt(self, a1):
        v1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        v2 = 0
        for v3 in range(len(a1)):
            if v3 > 0 and v1[a1[v3]] > v1[a1[v3 - 1]]:
                v2 += v1[a1[v3]] - 2 * v1[a1[v3 - 1]]
            else:
                v2 += v1[a1[v3]]
        return v2
