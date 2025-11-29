class Solution:
    def diameter(self, root):
        if not root:
            return 0
        self.max_length = 0

        def dfs(node):
            h1 = -1
            h2 = -1
            for c in node.children:
                ch = dfs(c)
                if ch > h1:
                    h2 = h1
                    h1 = ch
                elif ch > h2:
                    h2 = ch
            if node.children:
                arm1 = 1 + h1
                if h2 >= 0:
                    self.max_length = max(self.max_length, arm1 + 1 + h2)
                else:
                    self.max_length = max(self.max_length, arm1)
            return 1 + h1 if h1 >= 0 else 0

        dfs(root)
        return self.max_length
