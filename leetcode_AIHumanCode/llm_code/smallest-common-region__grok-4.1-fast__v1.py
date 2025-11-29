class Solution:
    def findSmallestRegion(self, regions, region1, region2):
        parent = {}
        for group in regions:
            head = group[0]
            for child in group[1:]:
                parent[child] = head

        def climb_to_root(start):
            trail = []
            pos = start
            while pos in parent:
                trail.append(pos)
                pos = parent[pos]
            trail.append(pos)
            return trail[::-1]

        trail1 = climb_to_root(region1)
        trail2 = climb_to_root(region2)
        idx = 0
        max_match = min(len(trail1), len(trail2))
        while idx < max_match and trail1[idx] == trail2[idx]:
            idx += 1
        return trail1[idx - 1]
