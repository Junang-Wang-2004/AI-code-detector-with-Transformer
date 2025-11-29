class Solution:
    def kthSmallest(self, root, k):
        def search(node, cnt):
            if not node:
                return None
            left_res = search(node.left, cnt)
            if left_res is not None:
                return left_res
            cnt[0] -= 1
            if cnt[0] == 0:
                return node.val
            return search(node.right, cnt)

        return search(root, [k])
