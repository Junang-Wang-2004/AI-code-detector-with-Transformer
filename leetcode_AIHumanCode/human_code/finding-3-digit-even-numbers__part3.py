# Time:  O(1) ~ O(n), n is 10^3
# Space: O(1)
import collections


class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution3(object):
    def findEvenNumbers(self, digits):
        """
        """
        k = 3
        def backtracking(curr, dummy, result):
            if len(curr) == k:
                result.append(reduce(lambda x, y: x*10+y, curr))
                return
            node = dummy.right
            while node:
                if (not curr and node.val[0] == 0) or (len(curr) == k-1 and node.val[0]%2 != 0):
                    node = node.right
                    continue
                node.val[1] -= 1
                if node.val[1] == 0:
                    if node.left:
                        node.left.right = node.right
                    if node.right:
                        node.right.left = node.left
                curr.append(node.val[0])
                backtracking(curr, dummy, result)
                curr.pop()
                if node.val[1] == 0:
                    if node.left:
                        node.left.right = node
                    if node.right:
                        node.right.left = node
                node.val[1] += 1
                node = node.right

        prev = dummy = Node()
        for digit, cnt in sorted(map(list, iter(collections.Counter(digits).items()))):
            prev.right = Node(val=[digit, cnt], left=prev)
            prev = prev.right
        result = []
        backtracking([], dummy, result)
        return result


