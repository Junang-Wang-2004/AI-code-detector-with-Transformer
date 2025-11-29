# Time:  O(n)
# Space: O(h)
# dfs solution with recursion
class Solution2(object):
    def balanceBST(self, root):
        """
        """
        def inorderTraversalHelper(node, arr):
            if not node:
                return
            inorderTraversalHelper(node.left, arr)
            arr.append(node.val)
            inorderTraversalHelper(node.right, arr)
        
        def sortedArrayToBstHelper(arr, i, j):
            if i >= j:
                return None
            mid = i + (j-i)//2
            node = TreeNode(arr[mid])
            node.left = sortedArrayToBstHelper(arr, i, mid)
            node.right = sortedArrayToBstHelper(arr, mid+1, j)
            return node
        
        arr = []
        inorderTraversalHelper(root, arr)
        return sortedArrayToBstHelper(arr, 0, len(arr))
