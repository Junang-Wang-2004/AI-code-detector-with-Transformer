class Solution(object):
    def findDistance(self, root, p, q):
        def get_path(start, target):
            if not start:
                return []
            stk = [(start, [start])]
            while stk:
                curr, trail = stk.pop()
                if curr.val == target:
                    return trail
                for nxt in (curr.right, curr.left):
                    if nxt:
                        stk.append((nxt, trail + [nxt]))
            return []

        route_p = get_path(root, p)
        route_q = get_path(root, q)
        idx = 0
        length = min(len(route_p), len(route_q))
        while idx < length and route_p[idx] == route_q[idx]:
            idx += 1
        return len(route_p) - idx + len(route_q) - idx
