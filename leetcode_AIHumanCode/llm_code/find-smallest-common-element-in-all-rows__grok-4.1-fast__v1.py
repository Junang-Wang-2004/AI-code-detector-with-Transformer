class Solution(object):
    def smallestCommonElement(self, mat):
        if not mat:
            return -1
        candidates = sorted(set(mat[0]))
        for row in mat[1:]:
            row_elements = set(row)
            filtered = [num for num in candidates if num in row_elements]
            candidates = filtered
            if not candidates:
                return -1
        return candidates[0] if candidates else -1
