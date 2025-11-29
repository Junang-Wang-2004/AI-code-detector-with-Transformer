# Time:  ctor:  O(n)
#        query: O(klogn), k = log2(Q/ERROR_RATE)
# Space: O(n)

import collections
import random
import bisect


class MajorityChecker(object):

    def __init__(self, arr):
        """
        """
        Q, ERROR_RATE = 10000, 0.001
        self.__K = int(Q/ERROR_RATE).bit_length()  # floor(log2(Q/ERROR_RATE))+1 = 24
        self.__arr = arr
        self.__inv_idx = collections.defaultdict(list)
        for i, x in enumerate(self.__arr):
            self.__inv_idx[x].append(i)

    def query(self, left, right, threshold):
        """
        """
        def count(inv_idx, m, left, right):
            return bisect.bisect_right(inv_idx[m], right) - \
                   bisect.bisect_left(inv_idx[m], left)

        for _ in range(self.__K):
            m = self.__arr[random.randint(left, right)]
            if count(self.__inv_idx, m, left, right) >= threshold:
                return m
        return -1


