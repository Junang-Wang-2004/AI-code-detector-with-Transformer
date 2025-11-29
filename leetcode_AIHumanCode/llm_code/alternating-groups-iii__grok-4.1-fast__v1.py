from sortedcontainers import SortedList

class Solution:
    def numberOfAlternatingGroups(self, colors, queries):
        n = len(colors)
        bads = SortedList()
        class Fenwick:
            def __init__(self, sz):
                self.size = sz
                self.tree = [0] * (sz + 1)
            def upd(self, i, v):
                while i <= self.size:
                    self.tree[i] += v
                    i += i & -i
            def pre(self, i):
                s = 0
                while i > 0:
                    s += self.tree[i]
                    i -= i & -i
                return s
        ft_cnt = Fenwick(n)
        ft_sm = Fenwick(n)
        def add_bad(pos):
            bads.add(pos)
            ln = len(bads)
            if ln == 1:
                ft_cnt.upd(n, 1)
                ft_sm.upd(n, n)
                return
            cidx = bads.index(pos)
            lidx = (cidx - 1) % ln
            ridx = (cidx + 1) % ln
            ppos = bads[lidx]
            rpos = bads[ridx]
            bigl = ((rpos - ppos - 1) % n) + 1
            ft_cnt.upd(bigl, -1)
            ft_sm.upd(bigl, -bigl)
            gl1 = (pos - ppos) % n
            ft_cnt.upd(gl1, 1)
            ft_sm.upd(gl1, gl1)
            gl2 = (rpos - pos) % n
            ft_cnt.upd(gl2, 1)
            ft_sm.upd(gl2, gl2)
        def rem_bad(pos):
            if not bads:
                return
            ln = len(bads)
            cidx = bads.index(pos)
            if ln == 1:
                ft_cnt.upd(n, -1)
                ft_sm.upd(n, -n)
                bads.pop(cidx)
                return
            lidx = (cidx - 1) % ln
            ridx = (cidx + 1) % ln
            ppos = bads[lidx]
            rpos = bads[ridx]
            bigl = ((rpos - ppos - 1) % n) + 1
            ft_cnt.upd(bigl, 1)
            ft_sm.upd(bigl, bigl)
            gl1 = (pos - ppos) % n
            ft_cnt.upd(gl1, -1)
            ft_sm.upd(gl1, -gl1)
            gl2 = (rpos - pos) % n
            ft_cnt.upd(gl2, -1)
            ft_sm.upd(gl2, -gl2)
            bads.pop(cidx)
        for j in range(n):
            if colors[j] == colors[(j + 1) % n]:
                add_bad(j)
        ans = []
        for q in queries:
            t = q[0]
            if t == 1:
                ll = q[1]
                if len(bads) == 0:
                    ans.append(n)
                else:
                    cn = ft_cnt.pre(n) - ft_cnt.pre(ll - 1)
                    su = ft_sm.pre(n) - ft_sm.pre(ll - 1)
                    ans.append(su - (ll - 1) * cn)
            else:
                idx = q[1]
                col = q[2]
                if colors[idx] == col:
                    continue
                pedge = (idx - 1) % n
                nedge = (idx + 1) % n
                opb = (colors[pedge] == colors[idx])
                onb = (colors[idx] == colors[nedge])
                colors[idx] = col
                npb = (colors[pedge] == colors[idx])
                nnb = (colors[idx] == colors[nedge])
                if opb != npb:
                    if npb:
                        add_bad(pedge)
                    else:
                        rem_bad(pedge)
                if onb != nnb:
                    if nnb:
                        add_bad(idx)
                    else:
                        rem_bad(idx)
        return ans
