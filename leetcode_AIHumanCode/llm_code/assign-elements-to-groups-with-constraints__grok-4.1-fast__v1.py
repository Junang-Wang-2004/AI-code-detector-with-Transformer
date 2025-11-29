class Solution(object):
    def assignElements(self, groups, elements):
        if not groups:
            return []
        maxg = max(groups)
        table = [-1] * (maxg + 1)
        for idx, div in enumerate(elements):
            if div > maxg or table[div] != -1:
                continue
            pos = div
            while pos <= maxg:
                if table[pos] == -1:
                    table[pos] = idx
                pos += div
        return [table[g] for g in groups]
