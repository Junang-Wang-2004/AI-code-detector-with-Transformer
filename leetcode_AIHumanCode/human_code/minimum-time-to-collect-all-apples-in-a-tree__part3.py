# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def minTime(self, n, edges, hasApple):
        """
        """
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        result = [0]
        s = [(1, (-1, 0, result))]
        while s:
            step, params = s.pop()
            if step == 1:
                par, node, ret = params
                tmp = [int(hasApple[node])]
                s.append((3, (tmp, ret)))
                for nei in reversed(graph[node]):
                    if nei == par:
                        continue
                    new_ret = [0]
                    s.append((2, (new_ret, tmp, ret)))
                    s.append((1, (node, nei, new_ret)))
            elif step == 2:
                new_ret, tmp, ret = params
                ret[0] += new_ret[0]
                tmp[0] |= bool(new_ret[0])
            else:
                tmp, ret = params
                ret[0] += tmp[0]
        return 2*max(result[0]-1, 0)


