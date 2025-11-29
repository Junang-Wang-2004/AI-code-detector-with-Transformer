class Solution:
    def minimumDistance(self, nums):
        positions = {}
        for idx, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(idx)
        minimum = float('inf')
        for pos_list in positions.values():
            n = len(pos_list)
            if n >= 3:
                for start in range(n - 2):
                    distance = 2 * (pos_list[start + 2] - pos_list[start])
                    if distance < minimum:
                        minimum = distance
        return minimum if minimum != float('inf') else -1
