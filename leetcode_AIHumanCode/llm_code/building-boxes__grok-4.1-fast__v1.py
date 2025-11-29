class Solution(object):
    def minimumBoxes(self, n):
        layer = 0
        accum = 0
        while True:
            next_accum = accum + (layer + 1) * (layer + 2) // 2
            if next_accum > n:
                break
            accum = next_accum
            layer += 1
        leftover = n - accum
        extra = 0
        current_tri = 0
        while current_tri < leftover:
            extra += 1
            current_tri = extra * (extra + 1) // 2
        result = layer * (layer + 1) // 2 + extra
        return result
