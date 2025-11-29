# Time:  O(n^3)
# Space: O(n^2)

class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        """
        def floydWarshall(n, graph): 
            reachable = set([x[0]*n+x[1] for x in graph]) 
            for k in range(n): 
                for i in range(n): 
                    for j in range(n): 
                        if i*n+j not in reachable and (i*n+k in reachable and k*n+j in reachable):
                            reachable.add(i*n+j)
            return reachable

        reachable = floydWarshall(n, prerequisites)
        return [i*n+j in reachable for i, j in queries]


