from collections import deque

class Solution:
    def replaceValueInTree(self, root):
        if not root:
            return root
        que = deque([(root, root.val)])
        while que:
            lv_sum = sum(nd.val for nd, _ in que)
            nxt_que = deque()
            while que:
                nd, grp = que.popleft()
                nd.val = lv_sum - grp
                ch_sum = 0
                if nd.left:
                    ch_sum += nd.left.val
                if nd.right:
                    ch_sum += nd.right.val
                if nd.left:
                    nxt_que.append((nd.left, ch_sum))
                if nd.right:
                    nxt_que.append((nd.right, ch_sum))
            que = nxt_que
        return root
