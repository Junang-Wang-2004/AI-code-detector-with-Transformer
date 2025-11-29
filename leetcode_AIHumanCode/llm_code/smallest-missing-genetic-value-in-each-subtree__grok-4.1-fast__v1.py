class Solution(object):
    def smallestMissingValueSubtree(self, parents, nums):
        n = len(parents)
        answer = [1] * n
        one_node = -1
        for idx in range(n):
            if nums[idx] == 1:
                one_node = idx
                break
        if one_node == -1:
            return answer
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)
        covered = set()
        here = one_node
        came_from = -1
        while here >= 0:
            if nums[here] not in covered:
                covered.add(nums[here])
            for ch in children[here]:
                if ch == came_from:
                    continue
                stk = [ch]
                while stk:
                    v = stk.pop()
                    if nums[v] in covered:
                        continue
                    covered.add(nums[v])
                    for gch in children[v]:
                        stk.append(gch)
            mex_val = 1
            while mex_val in covered:
                mex_val += 1
            answer[here] = mex_val
            came_from = here
            here = parents[here]
        return answer
