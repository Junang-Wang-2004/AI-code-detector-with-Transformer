from collections import defaultdict, deque

class Solution:
    def sortItems(self, n, m, group, beforeItems):
        groups = group[:]
        total_groups = m
        for i in range(n):
            if groups[i] == -1:
                groups[i] = total_groups
                total_groups += 1
        items_by_group = [[] for _ in range(total_groups)]
        for i in range(n):
            items_by_group[groups[i]].append(i)
        group_adj = defaultdict(set)
        group_indeg = defaultdict(int)
        local_adj = [defaultdict(set) for _ in range(total_groups)]
        local_indeg = [defaultdict(int) for _ in range(total_groups)]
        for i in range(n):
            gi = groups[i]
            for j in beforeItems[i]:
                gj = groups[j]
                if gi == gj:
                    if i not in local_adj[gi][j]:
                        local_adj[gi][j].add(i)
                        local_indeg[gi][i] += 1
                else:
                    if gi not in group_adj[gj]:
                        group_adj[gj].add(gi)
                        group_indeg[gi] += 1
        def kahn(adj, indeg, nodes):
            q = deque(nd for nd in nodes if indeg[nd] == 0)
            order = []
            while q:
                nd = q.popleft()
                order.append(nd)
                for neigh in adj[nd]:
                    indeg[neigh] -= 1
                    if indeg[neigh] == 0:
                        q.append(neigh)
            return order if len(order) == len(nodes) else None
        all_groups = list(range(total_groups))
        group_order = kahn(group_adj, group_indeg, all_groups)
        if group_order is None:
            return []
        result = []
        for g in group_order:
            grp_items = items_by_group[g]
            grp_order = kahn(local_adj[g], local_indeg[g], grp_items)
            if grp_order is None:
                return []
            result.extend(grp_order)
        return result
