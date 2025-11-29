class Solution(object):
    def depthSum(self, nestedList):
        stk = [(nestedList, 1)]
        total = 0
        while stk:
            lst, d = stk.pop()
            for node in lst:
                if node.isInteger():
                    total += node.getInteger() * d
                else:
                    stk.append((node.getList(), d + 1))
        return total
