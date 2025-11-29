# Time:  O(n)
# Space: O(h)
import collections


class Solution2(object):
    def countPairs(self, root, distance):
        """
        """
        def dfs(distance, node):
            if not node:
                return 0, collections.Counter()
            if not node.left and not node.right:
                return 0, collections.Counter([0])
            left, right = dfs(distance, node.left), dfs(distance, node.right)
            result = left[0]+right[0]
            for left_d, left_c in left[1].items():
                for right_d,right_c in right[1].items():
                    if left_d+right_d+2 <= distance:
                        result += left_c*right_c
            return result, collections.Counter({k+1:v for k,v in (left[1]+right[1]).items()})
        
        return dfs(distance, root)[0]
