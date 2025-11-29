# Time:  ctor:  O(n)
#        query: O(sqrt(n)*logn)
# Space: O(n)
import collections
import bisect


class MajorityChecker2(object):

    def __init__(self, arr):
        """
        """
        self.__arr = arr
        self.__inv_idx = collections.defaultdict(list)
        for i, x in enumerate(self.__arr):
            self.__inv_idx[x].append(i)
        self.__bound = int(round((len(arr)**0.5)))
        self.__majorities = [i for i, group in self.__inv_idx.items() if len(group) >= self.__bound]

    def query(self, left, right, threshold):
        """
        """
        def count(inv_idx, m, left, right):
            return bisect.bisect_right(inv_idx[m], right) - \
                   bisect.bisect_left(inv_idx[m], left)

        def boyer_moore_majority_vote(nums, left, right):
            m, cnt = nums[left], 1
            for i in range(left+1, right+1):
                if m == nums[i]:
                    cnt += 1
                else:
                    cnt -= 1
                    if cnt == 0:
                        m = nums[i]
                        cnt = 1
            return m

        if right-left+1 < self.__bound:
            m = boyer_moore_majority_vote(self.__arr, left, right)
            if count(self.__inv_idx, m, left, right) >= threshold:
                return m
        else:
            for m in self.__majorities:
                if count(self.__inv_idx, m, left, right) >= threshold:
                    return m
        return -1


