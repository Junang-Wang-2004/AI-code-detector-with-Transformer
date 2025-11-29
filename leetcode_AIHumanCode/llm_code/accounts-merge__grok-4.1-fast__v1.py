from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        parent = {}
        rank = {}
        email_name = {}

        def find(email):
            if parent[email] != email:
                parent[email] = find(parent[email])
            return parent[email]

        def unite(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1

        for record in accounts:
            owner = record[0]
            addresses = record[1:]
            if addresses:
                primary = addresses[0]
                for addr in addresses:
                    if addr not in parent:
                        parent[addr] = addr
                        rank[addr] = 0
                        email_name[addr] = owner
                for addr in addresses[1:]:
                    unite(primary, addr)

        components = defaultdict(list)
        for addr in parent:
            components[find(addr)].append(addr)

        res = []
        for addr_list in components.values():
            addr_list.sort()
            res.append([email_name[addr_list[0]]] + addr_list)
        return res
