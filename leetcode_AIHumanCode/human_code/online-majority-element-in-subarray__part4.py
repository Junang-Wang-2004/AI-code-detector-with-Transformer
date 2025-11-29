# Time:  ctor:  O(n)
#        query: O(sqrt(n)*logn)
# Space: O(n)
import collections
import bisect


class MajorityChecker4(object):

    def __init__(self, arr):
        """
        """
        self.__arr = arr
        self.__inv_idx = collections.defaultdict(list)
        for i, x in enumerate(self.__arr):
            self.__inv_idx[x].append(i)
        self.__bucket_size = int(round((len(arr)**0.5)))
        self.__bucket_majorities = []
        for left in range(0, len(self.__arr), self.__bucket_size):
            right = min(left+self.__bucket_size-1, len(self.__arr)-1)
            self.__bucket_majorities.append(self.__boyer_moore_majority_vote(self.__arr, left, right))

    def query(self, left, right, threshold):
        """
        """
        def count(inv_idx, m, left, right):
            return bisect.bisect_right(inv_idx[m], right) - \
                   bisect.bisect_left(inv_idx[m], left)

        l, r = left//self.__bucket_size, right//self.__bucket_size
        if l == r:
            m = self.__boyer_moore_majority_vote(self.__arr, left, right)
            if count(self.__inv_idx, m, left, right) >= threshold:
                return m
            return -1
        else:
            m = self.__boyer_moore_majority_vote(self.__arr, left, (l+1)*self.__bucket_size-1)
            if count(self.__inv_idx, m, left, right) >= threshold:
                return m
            m = self.__boyer_moore_majority_vote(self.__arr, r*self.__bucket_size, right)
            if count(self.__inv_idx, m, left, right) >= threshold:
                return m
            for i in range(l+1, r):
                if count(self.__inv_idx, self.__bucket_majorities[i], left, right) >= threshold:
                    return self.__bucket_majorities[i]
            return -1
    
    def __boyer_moore_majority_vote(self, nums, left, right):
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
