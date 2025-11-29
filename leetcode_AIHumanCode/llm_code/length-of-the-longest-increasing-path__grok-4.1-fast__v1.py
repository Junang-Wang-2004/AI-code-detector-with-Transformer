class Solution(object):
    def maxPathLength(self, points, index):
        tgt = points[index]
        tgt_x, tgt_y = tgt[0], tgt[1]
        
        candidates_left = [pt for pt in points if pt[0] < tgt_x and pt[1] < tgt_y]
        candidates_left.sort(key=lambda pt: (pt[0], -pt[1]))
        ys_left = [pt[1] for pt in candidates_left]
        
        candidates_right = [pt for pt in points if pt[0] > tgt_x and pt[1] > tgt_y]
        candidates_right.sort(key=lambda pt: (pt[0], -pt[1]))
        ys_right = [pt[1] for pt in candidates_right]
        
        def compute_lis_len(sequence):
            if not sequence:
                return 0
            min_tails = []
            for val in sequence:
                l, r = 0, len(min_tails)
                while l < r:
                    m = (l + r) // 2
                    if min_tails[m] < val:
                        l = m + 1
                    else:
                        r = m
                if l == len(min_tails):
                    min_tails.append(val)
                else:
                    min_tails[l] = val
            return len(min_tails)
        
        left_len = compute_lis_len(ys_left)
        right_len = compute_lis_len(ys_right)
        return left_len + 1 + right_len
