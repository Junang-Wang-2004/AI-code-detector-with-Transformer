# Time:  O(nlogn) ~ O(n^2)
# Space: O(n)
# BST solution.
class Solution3(object):
    def countSmaller(self, nums):
        """
        """
        res = [0] * len(nums)
        bst = self.BST()
        # Insert into BST and get left count.
        for i in reversed(range(len(nums))):
            bst.insertNode(nums[i])
            res[i] = bst.query(nums[i])

        return res

    class BST(object):
        class BSTreeNode(object):
            def __init__(self, val):
                self.val = val
                self.count = 0
                self.left = self.right = None

        def __init__(self):
            self.root = None

        # Insert node into BST.
        def insertNode(self, val):
            node = self.BSTreeNode(val)
            if not self.root:
                self.root = node
                return
            curr = self.root
            while curr:
                # Insert left if smaller.
                if node.val < curr.val:
                    curr.count += 1  # Increase the number of left children.
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = node
                        break
                else:  # Insert right if larger or equal.
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = node
                        break

        # Query the smaller count of the value.
        def query(self, val):
            count = 0
            curr = self.root
            while curr:
                # Insert left.
                if val < curr.val:
                    curr = curr.left
                elif val > curr.val:
                    count += 1 + curr.count  # Count the number of the smaller nodes.
                    curr = curr.right
                else:  # Equal.
                    return count + curr.count
            return 0

