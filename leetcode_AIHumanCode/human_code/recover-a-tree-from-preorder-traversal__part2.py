# Time:  O(n)
# Space: O(h)
# recursive solution
class Solution2(object):
    def recoverFromPreorder(self, S):
        """
        """
        def recoverFromPreorderHelper(S, level, i):
            j = i[0]
            while j < len(S) and S[j] == '-':
                j += 1 
            if level != j - i[0]:
                return None
            i[0] = j
            while j < len(S) and S[j] != '-':
                j += 1
            node = TreeNode(int(S[i[0]:j]))
            i[0] = j
            node.left = recoverFromPreorderHelper(S, level+1, i)
            node.right = recoverFromPreorderHelper(S, level+1, i)
            return node

        return recoverFromPreorderHelper(S, 0, [0])
