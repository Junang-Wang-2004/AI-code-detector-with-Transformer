class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def pathSum(self, a1, a2):

        def collect_paths(a1, a2):
            if not a1:
                return []
            if not a1.left and (not a1.right):
                return [[a1.val]] if a1.val == a2 else []
            v1 = collect_paths(a1.left, a2 - a1.val)
            v2 = collect_paths(a1.right, a2 - a1.val)
            v3 = v1 + v2
            return [[a1.val] + path for v4 in v3]
        return collect_paths(a1, a2)
