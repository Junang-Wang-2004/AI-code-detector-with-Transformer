class Solution:
    def maximumSetSize(self, nums1, nums2):
        unique1 = set(nums1)
        unique2 = set(nums2)
        excl1 = len(unique1.difference(unique2))
        excl2 = len(unique2.difference(unique1))
        comm = len(unique1.intersection(unique2))
        quota = len(nums1) // 2
        sel_ex1 = min(excl1, quota)
        sel_ex2 = min(excl2, quota)
        spare1 = quota - sel_ex1
        spare2 = quota - sel_ex2
        sel_comm = min(comm, spare1 + spare2)
        return sel_ex1 + sel_ex2 + sel_comm
