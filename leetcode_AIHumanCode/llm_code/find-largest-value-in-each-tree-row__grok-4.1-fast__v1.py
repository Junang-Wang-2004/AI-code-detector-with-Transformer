from collections import deque

class Solution:
    def largestValues(self, root):
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            mx = float('-inf')
            sz = len(q)
            for _ in range(sz):
                nd = q.popleft()
                mx = max(mx, nd.val)
                if nd.left:
                    q.append(nd.left)
                if nd.right:
                    q.append(nd.right)
            ans.append(mx)
        return ans
