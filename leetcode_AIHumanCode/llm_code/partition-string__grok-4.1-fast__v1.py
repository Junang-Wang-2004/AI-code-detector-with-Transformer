class Solution(object):
    def partitionString(self, s):
        graph = [[-1] * 26]
        state = 0
        ans = []
        seg = []
        def alloc():
            graph.append([-1] * 26)
            return len(graph) - 1
        for c in s:
            seg.append(c)
            k = ord(c) - ord('a')
            if graph[state][k] == -1:
                graph[state][k] = alloc()
                state = 0
            else:
                state = graph[state][k]
            if state:
                continue
            ans.append(''.join(seg))
            seg = []
        if seg:
            ans.append(''.join(seg))
        return ans
