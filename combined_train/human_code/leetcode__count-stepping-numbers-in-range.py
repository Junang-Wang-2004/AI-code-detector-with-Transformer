from functools import reduce

class C1(object):

    def countSteppingNumbers(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7

        def f(a1):
            v1 = [[0] * 10 for v2 in range(2)]
            for v3 in range(1, ord(a1[0]) - ord('0') + 1):
                v1[0][v3] = 1
            v4 = True
            for v5 in range(1, len(a1)):
                for v3 in range(10):
                    v1[v5 % 2][v3] = int(v3 != 0)
                    if v3 - 1 >= 0:
                        v1[v5 % 2][v3] = (v1[v5 % 2][v3] + (v1[(v5 - 1) % 2][v3 - 1] - int(v4 and ord(a1[v5 - 1]) - ord('0') == v3 - 1 and (v3 > ord(a1[v5]) - ord('0'))))) % v1
                    if v3 + 1 < 10:
                        v1[v5 % 2][v3] = (v1[v5 % 2][v3] + (v1[(v5 - 1) % 2][v3 + 1] - int(v4 and ord(a1[v5 - 1]) - ord('0') == v3 + 1 and (v3 > ord(a1[v5]) - ord('0'))))) % v1
                if abs(ord(a1[v5]) - ord(a1[v5 - 1])) != 1:
                    v4 = False
            return reduce(lambda x, y: (x + y) % v1, v1[(len(a1) - 1) % 2])
        return (f(a2) - f(str(int(a1) - 1))) % v1
