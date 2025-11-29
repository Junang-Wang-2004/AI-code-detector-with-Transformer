# Time:  ctor:  O(nlogn)
#        query: O((logn)^2)
# Space: O(n)
import functools


class SegmentTreeRecu(object):  # 0-based index
    def __init__(self, nums, count):
        """
        initialize your data structure here.
        """
        N = len(nums)
        self.__original_length = N
        self.__tree_length = 2**(N.bit_length() + (N&(N-1) != 0))-1
        self.__tree = [-1 for _ in range(self.__tree_length)]
        self.__count = count
        self.__constructTree(nums, 0, self.__original_length-1, 0)

    def query(self, i, j):
        return self.__queryRange(i, j, 0, self.__original_length-1, 0)

    def __constructTree(self, nums, left, right, idx):
        if left > right:
             return
        if left == right:
            self.__tree[idx] = nums[left]
            return 
        mid = left + (right-left)//2
        self.__constructTree(nums, left, mid, idx*2 + 1)
        self.__constructTree(nums, mid+1, right, idx*2 + 2)
        if self.__tree[idx*2 + 1] != -1 and \
           self.__count(self.__tree[idx*2 + 1], left, right)*2 > right-left+1:
            self.__tree[idx] = self.__tree[idx*2 + 1] 
        elif self.__tree[idx*2 + 2] != -1 and \
             self.__count(self.__tree[idx*2 + 2], left, right)*2 > right-left+1:
            self.__tree[idx] = self.__tree[idx*2 + 2] 

    def __queryRange(self, range_left, range_right, left, right, idx):
        if left > right:
            return (-1, -1)
        if right < range_left or left > range_right:
            return (-1, -1)
        if range_left <= left and right <= range_right:
            if self.__tree[idx] != -1:
                c = self.__count(self.__tree[idx], range_left, range_right)
                if c*2 > range_right-range_left+1:
                    return (self.__tree[idx], c)
        else:
            mid = left + (right-left)//2
            result = self.__queryRange(range_left, range_right, left, mid, idx*2 + 1)
            if result[0] != -1:
                return result
            result = self.__queryRange(range_left, range_right, mid + 1, right, idx*2 + 2)
            if result[0] != -1:
                return result
        return (-1, -1)


class MajorityChecker3(object):

    def __init__(self, arr):
        """
        """
        def count(inv_idx, m, left, right):
            return bisect.bisect_right(inv_idx[m], right) - \
                   bisect.bisect_left(inv_idx[m], left)

        self.__arr = arr
        self.__inv_idx = collections.defaultdict(list)
        for i, x in enumerate(self.__arr):
            self.__inv_idx[x].append(i)
        self.__segment_tree = SegmentTreeRecu(arr, functools.partial(count, self.__inv_idx))

    def query(self, left, right, threshold):
        """
        """
        result = self.__segment_tree.query(left, right)
        if result[1] >= threshold:
            return result[0]
        return -1


