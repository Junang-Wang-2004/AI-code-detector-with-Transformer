import collections

class Solution(object):
    def findShortestPath(self, master):
        dirs = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]
        opposites = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

        def traverse(curr, tgt_ref, agent, vis, nbrs):
            if tgt_ref[0] is None and agent.isTarget():
                tgt_ref[0] = curr
            vis.add(curr)
            for dr, dc, cmd in dirs:
                nxt_pos = (curr[0] + dr, curr[1] + dc)
                if not agent.canMove(cmd):
                    continue
                nbrs[curr].add(nxt_pos)
                nbrs[nxt_pos].add(curr)
                if nxt_pos in vis:
                    continue
                agent.move(cmd)
                traverse(nxt_pos, tgt_ref, agent, vis, nbrs)
                agent.move(opposites[cmd])

        def shortest_route(net, src, dest):
            from collections import deque
            if src == dest:
                return 0
            seen = set([src])
            q = deque([src])
            lvl = 0
            while q:
                lvl += 1
                sz = len(q)
                for _ in range(sz):
                    at = q.popleft()
                    for nb in net[at]:
                        if nb in seen:
                            continue
                        if nb == dest:
                            return lvl
                        seen.add(nb)
                        q.append(nb)
            return -1

        net = collections.defaultdict(set)
        tgt_ref = [None]
        init = (0, 0)
        traverse(init, tgt_ref, master, set(), net)
        if tgt_ref[0] is None:
            return -1
        return shortest_route(net, init, tgt_ref[0])
