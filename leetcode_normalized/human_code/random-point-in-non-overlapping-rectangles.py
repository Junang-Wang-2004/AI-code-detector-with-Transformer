import random
import bisect

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__rects = list(a1)
        self.__prefix_sum = [(x[2] - x[0] + 1) * (x[3] - x[1] + 1) for v1 in a1]
        for v2 in range(1, len(self.__prefix_sum)):
            self.__prefix_sum[v2] += self.__prefix_sum[v2 - 1]

    def pick(self):
        """
        """
        v1 = random.randint(0, self.__prefix_sum[-1] - 1)
        v2 = bisect.bisect_right(self.__prefix_sum, v1)
        v3 = self.__rects[v2]
        v4, v5 = (v3[2] - v3[0] + 1, v3[3] - v3[1] + 1)
        v6 = self.__prefix_sum[v2] - v4 * v5
        return [v3[0] + (v1 - v6) % v4, v3[1] + (v1 - v6) // v4]
