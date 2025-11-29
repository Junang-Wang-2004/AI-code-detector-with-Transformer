class C1(object):

    def tree2str(self, a1):
        """
        """
        if not a1:
            return ''
        v1 = str(a1.val)
        if a1.left or a1.right:
            v1 += '(' + self.tree2str(a1.left) + ')'
        if a1.right:
            v1 += '(' + self.tree2str(a1.right) + ')'
        return v1
