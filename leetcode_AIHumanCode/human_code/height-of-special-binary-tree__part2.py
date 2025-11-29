# Time:  O(n)
# Space: O(w)
# bfs
class Solution2(object):
    def heightOfTree(self, root):
        """
        """
        result = -1
        q = [root]
        while q:
            new_q = []
            for u in q:
                if u.left and u.left.right != u:
                    new_q.append(u.left)
                if u.right and u.right.left != u:
                    new_q.append(u.right)
            q = new_q
            result += 1
        return result
