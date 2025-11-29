class Solution:
    def depthSumInverse(self, nestedList):
        queue = [(elem, 0) for elem in nestedList]
        level_totals = []
        maxdepth = 0
        while queue:
            current, level = queue.pop(0)
            maxdepth = max(maxdepth, level)
            while len(level_totals) <= level:
                level_totals.append(0)
            if current.isInteger():
                level_totals[level] += current.getInteger()
            else:
                for nested in current.getList():
                    queue.append((nested, level + 1))
        result = 0
        levels = len(level_totals)
        for idx, total_at_level in enumerate(level_totals):
            result += total_at_level * (levels - idx)
        return result
