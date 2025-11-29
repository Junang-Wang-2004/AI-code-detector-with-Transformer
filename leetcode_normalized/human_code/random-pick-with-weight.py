import random
import bisect

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__prefix_sum = list(a1)
        for v1 in range(1, len(a1)):
            self.__prefix_sum[v1] += self.__prefix_sum[v1 - 1]

    def pickIndex(self):
        """
        """
        v1 = random.randint(0, self.__prefix_sum[-1] - 1)
        return bisect.bisect_right(self.__prefix_sum, v1)
