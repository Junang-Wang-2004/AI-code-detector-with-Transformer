class C1(object):

    def countSteppingNumbers(self, a1, a2):
        """
        """
        v1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for v2 in range(1, a2):
            if v1[-1] >= a2:
                break
            v3 = v1[v2] % 10 - 1
            if v3 >= 0:
                v1.append(v1[v2] * 10 + v3)
            v4 = v1[v2] % 10 + 1
            if v4 <= 9:
                v1.append(v1[v2] * 10 + v4)
        v1.append(float('inf'))
        v5 = bisect.bisect_left(v1, a1)
        v6 = bisect.bisect_right(v1, a2)
        return v1[v5:v6]
