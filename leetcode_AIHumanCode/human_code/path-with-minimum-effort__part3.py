# Time:  O(m * n * logh)
# Space: O(m * n)
# bi-bfs solution
class Solution3(object):
    def minimumEffortPath(self, heights):
        """
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def check(heights, x):  # bi-bfs
            lookup = [[False]*len(heights[0]) for _ in range(len(heights))]
            left, right = {(0, 0)}, {(len(heights)-1, len(heights[0])-1)}
            while left:
                for r, c in left:
                    lookup[r][c] = True
                new_left = set()
                for r, c in left:
                    if (r, c) in right: 
                        return True
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if not (0 <= nr < len(heights) and
                                0 <= nc < len(heights[0]) and
                                abs(heights[nr][nc]-heights[r][c]) <= x and
                                not lookup[nr][nc]):
                            continue
                        new_left.add((nr, nc))
                left = new_left
                if len(left) > len(right): 
                    left, right = right, left
            return False            
        

        left, right = 0, 10**6
        while left <= right:
            mid = left + (right-left)//2
            if check(heights, mid):
                right = mid-1
            else:
                left = mid+1
        return left


