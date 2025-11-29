class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def canMerge(self, a1):
        v1 = set()
        v2 = {}
        for v3 in a1:
            v2[v3.val] = v3
            v4 = [v3]
            while v4:
                v5 = v4.pop()
                if v5.left is None and v5.right is None and (v5 != v3):
                    v1.add(v5.val)
                if v5.right:
                    v4.append(v5.right)
                if v5.left:
                    v4.append(v5.left)
        v6 = None
        for v3 in a1:
            if v3.val not in v1:
                if v6 is not None:
                    return None
                v6 = v3
        if v6 is None:
            return None
        del v2[v6.val]

        def validate_and_merge(a1, a2, a3):
            if not a2 < a1.val < a3:
                return False
            if a1.left:
                v1 = a1.left.val
                if v1 in v1 and v1 in v2:
                    a1.left = v2[v1]
                    del v2[v1]
                if not validate_and_merge(a1.left, a2, a1.val):
                    return False
            if a1.right:
                v2 = a1.right.val
                if v2 in v1 and v2 in v2:
                    a1.right = v2[v2]
                    del v2[v2]
                if not validate_and_merge(a1.right, a1.val, a3):
                    return False
            return True
        if validate_and_merge(v6, float('-inf'), float('inf')) and (not v2):
            return v6
        return None
