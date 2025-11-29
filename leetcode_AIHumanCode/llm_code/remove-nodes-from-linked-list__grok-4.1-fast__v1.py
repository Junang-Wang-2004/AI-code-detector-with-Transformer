class Solution(object):
    def removeNodes(self, head):
        def process(node):
            if not node:
                return None, float('-inf')
            tail, tail_max = process(node.next)
            if node.val > tail_max:
                node.next = tail
                return node, node.val
            return tail, tail_max
        result, _ = process(head)
        return result
