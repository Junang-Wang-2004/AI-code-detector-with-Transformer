# Time:  O(n)
# Space: O(n)

import collections


# dfs solution with stack
class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        """
        children = collections.defaultdict(list)
        for child, parent in enumerate(manager):
            if parent != -1:
                children[parent].append(child)

        result = 0
        stk = [(headID, 0)]
        while stk:
            node, curr = stk.pop()
            curr += informTime[node]
            result = max(result, curr)
            if node not in children:
                continue
            for c in children[node]:
                stk.append((c, curr))
        return result

    
