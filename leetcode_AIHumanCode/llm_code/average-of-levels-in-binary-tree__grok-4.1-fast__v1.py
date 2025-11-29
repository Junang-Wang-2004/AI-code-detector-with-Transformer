from collections import deque


class Solution(object):
    def averageOfLevels(self, root):
        if not root:
            return []
        avgs = []
        bfs = deque([root])
        while bfs:
            sz = len(bfs)
            sm = 0
            for _ in range(sz):
                cur = bfs.popleft()
                sm += cur.val
                if cur.left:
                    bfs.append(cur.left)
                if cur.right:
                    bfs.append(cur.right)
            avgs.append(sm / sz)
        return avgs
