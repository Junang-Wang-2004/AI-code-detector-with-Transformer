# Time:  O(n)
# Space: O(n)
# dfs solution with recursion
class Solution2(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        """
        def dfs(informTime, children, node):
            return (max(dfs(informTime, children, c)
                        for c in children[node])
                    if node in children
                    else 0) + informTime[node]

        children = collections.defaultdict(list)
        for child, parent in enumerate(manager):
            if parent != -1:
                children[parent].append(child)
        return dfs(informTime, children, headID)
