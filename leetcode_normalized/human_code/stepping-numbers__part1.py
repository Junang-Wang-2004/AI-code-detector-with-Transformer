import bisect
v1 = int(2000000000.0)
v2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for v3 in range(1, v1):
    if v2[-1] >= v1:
        break
    v4 = v2[v3] % 10 - 1
    if v4 >= 0:
        v2.append(v2[v3] * 10 + v4)
    v5 = v2[v3] % 10 + 1
    if v5 <= 9:
        v2.append(v2[v3] * 10 + v5)
v2.append(float('inf'))

class C1(object):

    def countSteppingNumbers(self, a1, a2):
        """
        """
        v1 = bisect.bisect_left(v2, a1)
        v2 = bisect.bisect_right(v2, a2)
        return v2[v1:v2]
