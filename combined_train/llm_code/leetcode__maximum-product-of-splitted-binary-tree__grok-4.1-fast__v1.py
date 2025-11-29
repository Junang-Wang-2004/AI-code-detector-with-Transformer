class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def maxProduct(self, a1):
        v1 = 10 ** 9 + 7

        def compute_total(a1):
            return a1.val + compute_total(a1.left) + compute_total(a1.right) if a1 else 0
        v2 = compute_total(a1)
        v3 = 0

        def traverse(a1):
            nonlocal max_value
            if not a1:
                return 0
            v1 = a1.val + traverse(a1.left) + traverse(a1.right)
            v2 = max(v2, v1 * (v2 - v1))
            return v1
        traverse(a1)
        return v3 % v1
