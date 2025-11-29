class Solution(object):
    def componentValue(self, nums, edges):
        n = len(nums)
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        tree_total = sum(nums)
        def factorize(total):
            factors = []
            i = 1
            while i * i <= total:
                if total % i == 0:
                    factors.append(i)
                    if i != total // i:
                        factors.append(total // i)
                i += 1
            return sorted(set(factors), reverse=True)
        candidates = factorize(tree_total)
        def validate(part_sum):
            accum = nums[:]
            remains = [len(graph[j]) for j in range(n)]
            process = [j for j in range(n) if remains[j] == 1]
            while process:
                next_process = []
                for curr_node in process:
                    if accum[curr_node] > part_sum:
                        return False
                    if accum[curr_node] == part_sum:
                        accum[curr_node] = 0
                    for next_node in graph[curr_node]:
                        accum[next_node] += accum[curr_node]
                        remains[next_node] -= 1
                        if remains[next_node] == 1:
                            next_process.append(next_node)
                process = next_process
            return True
        for parts in candidates:
            if 2 <= parts <= n and validate(tree_total // parts):
                return parts - 1
        return 0
