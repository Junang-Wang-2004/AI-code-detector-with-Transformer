class Solution:
    def maxPartitionFactor(self, points):
        n = len(points)
        dists = set()
        for i in range(n):
            for j in range(i + 1, n):
                dx = abs(points[i][0] - points[j][0])
                dy = abs(points[i][1] - points[j][1])
                dists.add(dx + dy)
        dist_list = sorted(dists)
        if not dist_list:
            return 0

        def is_bip(max_d):
            colors = [-1] * n
            def color_comp(start):
                stack = [start]
                colors[start] = 0
                while stack:
                    u = stack.pop()
                    for v in range(n):
                        if v == u:
                            continue
                        dd = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                        if dd > max_d:
                            continue
                        if colors[v] == -1:
                            colors[v] = 1 - colors[u]
                            stack.append(v)
                        elif colors[v] == colors[u]:
                            return False
                return True
            for i in range(n):
                if colors[i] == -1:
                    if not color_comp(i):
                        return False
            return True

        left, right = 0, len(dist_list) - 1
        result = 0
        while left <= right:
            mid = left + (right - left) // 2
            if not is_bip(dist_list[mid]):
                result = dist_list[mid]
                right = mid - 1
            else:
                left = mid + 1
        return result
