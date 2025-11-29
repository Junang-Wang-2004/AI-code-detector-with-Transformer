class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        def build(rs, cs, len_):
            init_val = grid[rs][cs] == 1
            is_uniform = True
            for di in range(len_):
                ri = rs + di
                for dj in range(len_):
                    ci = cs + dj
                    if (grid[ri][ci] == 1) != init_val:
                        is_uniform = False
                        break
                if not is_uniform:
                    break
            if is_uniform:
                return Node(init_val, True, None, None, None, None)
            m = len_ // 2
            return Node(True, False,
                        build(rs, cs, m),
                        build(rs, cs + m, m),
                        build(rs + m, cs, m),
                        build(rs + m, cs + m, m))

        n = len(grid)
        return None if n == 0 else build(0, 0, n)
