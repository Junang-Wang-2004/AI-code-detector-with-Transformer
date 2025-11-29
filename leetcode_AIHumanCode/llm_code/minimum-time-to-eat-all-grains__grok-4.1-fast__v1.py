class Solution:
    def minimumTime(self, hens, grains):
        hens = sorted(hens)
        grains = sorted(grains)
        min_pos = min(hens[0], grains[0])
        max_pos = max(hens[-1], grains[-1])
        
        def can_cover(time):
            ptr = 0
            n = len(grains)
            for pos in hens:
                if ptr >= n:
                    return True
                dist = pos - grains[ptr]
                if dist > time:
                    return False
                if dist <= 0:
                    ext = time
                else:
                    dd = dist
                    opt1 = time - 2 * dd
                    opt2 = (time - dd) // 2
                    ext = max(opt1, opt2)
                farthest = pos + ext
                while ptr < n and grains[ptr] <= farthest:
                    ptr += 1
                if ptr >= n:
                    return True
            return ptr >= n
        
        low = 0
        high = 2 * (max_pos - min_pos)
        while low < high:
            m = (low + high) // 2
            if can_cover(m):
                high = m
            else:
                low = m + 1
        return low
