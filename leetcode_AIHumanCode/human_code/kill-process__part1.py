# Time:  O(n)
# Space: O(n)

import collections


# DFS solution.
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        """
        def killAll(pid, children, killed):
            killed.append(pid)
            for child in children[pid]:
                killAll(child, children, killed)

        result = []
        children = collections.defaultdict(set)
        for i in range(len(pid)):
            children[ppid[i]].add(pid[i])
        killAll(kill, children, result)
        return result


