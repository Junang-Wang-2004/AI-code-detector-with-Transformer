class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Codec(object):

    def serialize(self, root):
        if not root:
            return ""
        stk = [root]
        result = []
        while stk:
            curr = stk.pop()
            if curr:
                result.append(str(curr.val))
                stk.append(curr.right)
                stk.append(curr.left)
        return " ".join(result)

    def deserialize(self, data):
        nums = [int(x) for x in data.split()]
        idx = 0

        def build(lb, ub):
            nonlocal idx
            if idx >= len(nums) or not (lb < nums[idx] < ub):
                return None
            v = nums[idx]
            idx += 1
            node = TreeNode(v)
            node.left = build(lb, v)
            node.right = build(v, ub)
            return node

        return build(float('-inf'), float('inf'))
