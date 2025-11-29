# Time:  O(n)
# Space: O(w)
# bfs solution
class Solution2(object):
    def maxLevelSum(self, root):
        """
        """
        result, level, max_total = 0, 1, float("-inf")
        q = collections.deque([root])
        while q:
            total = 0
            for _ in range(len(q)):
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if total > max_total:
                result, max_total = level, total
            level += 1
        return result
