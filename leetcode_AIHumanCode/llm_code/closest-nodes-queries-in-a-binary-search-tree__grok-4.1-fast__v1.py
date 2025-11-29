class Solution(object):
    def closestNodes(self, root, queries):
        def find_floor_ceiling(node, target):
            floor = -1
            ceiling = -1
            curr = node
            while curr:
                if curr.val == target:
                    return [target, target]
                if curr.val < target:
                    floor = curr.val
                    curr = curr.right
                else:
                    ceiling = curr.val
                    curr = curr.left
            return [floor, ceiling]

        return [find_floor_ceiling(root, q) for q in queries]
