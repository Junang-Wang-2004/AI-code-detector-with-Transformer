# Time:  O(nlogn)
# Space: O(n)
# optimized from Solution5
class Solution4(object):
    def lengthOfLIS(self, nums):
        """
        """
        val_to_idx = {num:i for i, num in enumerate(sorted(set(nums)))}
        st = SegmentTree(len(val_to_idx))
        for x in nums:
            st.update(val_to_idx[x], val_to_idx[x], st.query(0, val_to_idx[x]-1)+1 if val_to_idx[x] >= 1 else 1)
        return st.query(0, len(val_to_idx)-1) if len(val_to_idx) >= 1 else 0


