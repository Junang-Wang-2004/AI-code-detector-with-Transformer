class Solution(object):
    def getDirections(self, root, startValue, destValue):
        def find_path(node, target):
            if not node:
                return None
            if node.val == target:
                return [node]
            leftp = find_path(node.left, target)
            if leftp is not None:
                return [node] + leftp
            rightp = find_path(node.right, target)
            if rightp is not None:
                return [node] + rightp
            return None

        pstart = find_path(root, startValue)
        pdest = find_path(root, destValue)
        idx = 0
        m = min(len(pstart), len(pdest))
        while idx < m and pstart[idx] == pdest[idx]:
            idx += 1
        result = 'U' * (len(pstart) - idx)
        for j in range(idx, len(pdest) - 1):
            if pdest[j + 1] == pdest[j].left:
                result += 'L'
            else:
                result += 'R'
        return result
