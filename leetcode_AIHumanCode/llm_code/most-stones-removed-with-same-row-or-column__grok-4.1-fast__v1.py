class Solution:
    def removeStones(self, stones):
        par = {}
        rnk = {}
        
        def locate(node):
            if node not in par:
                par[node] = node
                rnk[node] = 0
            if par[node] != node:
                par[node] = locate(par[node])
            return par[node]
        
        def link(u, v):
            pu, pv = locate(u), locate(v)
            if pu == pv:
                return
            if rnk[pu] < rnk[pv]:
                par[pu] = pv
            elif rnk[pu] > rnk[pv]:
                par[pv] = pu
            else:
                par[pv] = pu
                rnk[pu] += 1
        
        for row, col in stones:
            link('row' + str(row), 'col' + str(col))
        
        groups = {locate('row' + str(row)) for row, col in stones}
        return len(stones) - len(groups)
