# Time:  O(n * l^4)
# Space: O(n * l^2 + min(n * l^4, n^2)) = O(n * l^4)

import collections


# freq table, combinatorics
class Solution(object):
    def countPairs(self, nums):
        """
        """
        L = 7
        POW10 = [0]*L
        POW10[0] = 1
        for i in range(L-1):
            POW10[i+1] = POW10[i]*10
        cnt1 = collections.Counter(nums)
        adj = collections.defaultdict(list)
        cnt = list(cnt1.items())
        for idx in range(len(cnt)):
            adj[cnt[idx][0]].append(idx)
            for i in range(L):
                a = cnt[idx][0]//POW10[i]%10
                for j in range(i+1, L):
                    b = cnt[idx][0]//POW10[j]%10
                    if a == b:
                        continue
                    adj[cnt[idx][0]-a*(POW10[i]-POW10[j])+b*(POW10[i]-POW10[j])].append(idx)
        result = sum(v*(v-1)//2 for v in cnt1.values())
        lookup = set()
        for u in adj.keys():
            for i in range(len(adj[u])):
                v1 = cnt[adj[u][i]][1]
                for j in range(i+1, len(adj[u])):
                    v2 = cnt[adj[u][j]][1]
                    if (adj[u][i], adj[u][j]) in lookup:
                        continue
                    lookup.add((adj[u][i], adj[u][j]))
                    result += v1*v2
        return result


