import collections

class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.list1 = nums1
        self.list2 = nums2
        self.freq2 = collections.Counter(nums2)

    def add(self, index, val):
        old = self.list2[index]
        self.freq2[old] -= 1
        self.list2[index] += val
        self.freq2[self.list2[index]] += 1

    def count(self, tot):
        return sum(self.freq2[tot - x] for x in self.list1)
