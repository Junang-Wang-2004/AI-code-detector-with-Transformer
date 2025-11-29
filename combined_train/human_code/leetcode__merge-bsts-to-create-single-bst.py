class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def canMerge(self, a1):
        """
        """

        def find_leaves_and_roots(a1, a2, a3):
            for v1 in a1:
                a3[v1.val] = v1
                v2 = [v1]
                while v2:
                    v3 = []
                    for v4 in v2:
                        if v4.left is None and v4.right is None:
                            if v4 is not v1:
                                a2.add(v4.val)
                            continue
                        if v4.left:
                            v3.append(v4.left)
                        if v4.right:
                            v3.append(v4.right)
                    v2 = v3

        def find_root(a1, a2, a3):
            v1 = None
            for v2 in a1:
                if v2.val in leaf_vals_set:
                    continue
                if v1:
                    return None
                v1 = v2
            return v1

        def merge_bsts(a1, a2, a3):
            if not a1:
                return None
            del a3[a1.val]
            v1 = [(a1, float('-inf'), float('inf'))]
            while v1:
                v2 = []
                for v3, v4, v5 in v1:
                    if not v4 < v3.val < v5:
                        return None
                    if v3.left:
                        if v3.left.val in leaf_vals_set and v3.left.val in a3:
                            v3.left = a3[v3.left.val]
                            del a3[v3.left.val]
                        v2.append((v3.left, v4, v3.val))
                    if v3.right:
                        if v3.right.val in leaf_vals_set and v3.right.val in a3:
                            v3.right = a3[v3.right.val]
                            del a3[v3.right.val]
                        v2.append((v3.right, v3.val, v5))
                v1 = v2
            return a1 if not a3 else None
        v1, v2 = (set(), {})
        find_leaves_and_roots(a1, v1, v2)
        v3 = find_root(a1, v1, v2)
        return merge_bsts(v3, v1, v2)
