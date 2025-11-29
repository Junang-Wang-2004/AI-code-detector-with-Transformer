class Solution:
    def countRectangles(self, rect_list, query_pts):
        if not rect_list:
            return [0] * len(query_pts)
        max_height = max(h for _, h in rect_list)
        height_groups = [[] for _ in range(max_height + 1)]
        for width, height in rect_list:
            height_groups[height].append(width)
        for group in height_groups:
            group.sort()
        
        def num_greater_or_equal(srt_list, target):
            lo, hi = 0, len(srt_list)
            while lo < hi:
                md = (lo + hi) // 2
                if srt_list[md] >= target:
                    hi = md
                else:
                    lo = md + 1
            return len(srt_list) - lo
        
        ans = []
        for pwidth, pheight in query_pts:
            cnt = 0
            for h in range(pheight, max_height + 1):
                cnt += num_greater_or_equal(height_groups[h], pwidth)
            ans.append(cnt)
        return ans
