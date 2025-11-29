class Solution:
    def lowestCommonAncestor(self, p, q):
        path_from_p = []
        current = p
        while current:
            path_from_p.append(current)
            current = current.parent
        
        path_from_q = []
        current = q
        while current:
            path_from_q.append(current)
            current = current.parent
        
        pointer_p = len(path_from_p) - 1
        pointer_q = len(path_from_q) - 1
        while pointer_p >= 0 and pointer_q >= 0 and path_from_p[pointer_p] == path_from_q[pointer_q]:
            pointer_p -= 1
            pointer_q -= 1
        return path_from_p[pointer_p + 1]
