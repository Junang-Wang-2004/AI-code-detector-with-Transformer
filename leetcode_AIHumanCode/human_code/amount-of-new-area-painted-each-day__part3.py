# Time:  O(nlogr), r is the max position
# Space: O(r)
# segment tree
class SolutionTLE(object):
    def amountPainted(self, paint):
        """
        """
        result = []
        st = SegmentTree(max(e for _, e in paint))
        for s, e in paint:
            cnt = st.query(s, e-1)
            st.update(s, e-1, 1)
            result.append(st.query(s, e-1)-cnt)
        return result
