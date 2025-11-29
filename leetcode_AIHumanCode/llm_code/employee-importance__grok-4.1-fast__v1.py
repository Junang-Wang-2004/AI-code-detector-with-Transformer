class Solution(object):
    def getImportance(self, employees, target):
        imp = {e.id: e.importance for e in employees}
        adj = {e.id: e.subordinates for e in employees}
        def calc(node):
            return imp.get(node, 0) + sum(calc(c) for c in adj.get(node, []))
        return calc(target)
