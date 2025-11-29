# Time:  O(nlogn)
# Space: O(n)
# segment tree solution
class Solution2(object):
    def minOperations(self, target, arr):
        """
        """
        lookup = {x:i for i, x in enumerate(target)}
        st = SegmentTree(len(lookup))
        for x in arr:
            if x not in lookup:
                continue
            st.update(lookup[x], lookup[x], st.query(0, lookup[x]-1)+1 if lookup[x] >= 1 else 1)
        return len(target)-(st.query(0, len(lookup)-1) if len(lookup) >= 1 else 0)
