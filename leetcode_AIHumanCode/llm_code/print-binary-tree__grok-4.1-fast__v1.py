class Solution(object):
    def printTree(self, root):
        if not root:
            return []
        def depth(n):
            if not n:
                return 0
            return 1 + max(depth(n.left), depth(n.right))
        rows = depth(root)
        def span(n):
            if not n:
                return 0
            return 1 + 2 * max(span(n.left), span(n.right))
        cols = span(root)
        board = [['' for _ in range(cols)] for _ in range(rows)]
        q = []
        q.append((root, 0, cols // 2))
        while q:
            curr, r, c = q.pop(0)
            if curr:
                board[r][c] = str(curr.val)
                shift_amt = 1 << (rows - r - 2)
                if curr.left:
                    q.append((curr.left, r + 1, c - shift_amt))
                if curr.right:
                    q.append((curr.right, r + 1, c + shift_amt))
        return board
