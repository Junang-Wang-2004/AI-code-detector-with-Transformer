from sortedcontainers import SortedList

class Solution:
    def getResults(self, queries):
        add_values = sorted(q[1] for q in queries if q[0] == 1)
        ranks = {v: ii for ii, v in enumerate(add_values)}
        num = len(add_values)
        
        class MaxSegTree:
            def __init__(self, nn):
                self.nn = nn
                self.t = [0] * (4 * nn)
            
            def _upd(self, no, lo, hi, pos, newv):
                if lo == hi:
                    self.t[no] = newv
                    return
                md = (lo + hi) // 2
                if pos <= md:
                    self._upd(2 * no, lo, md, pos, newv)
                else:
                    self._upd(2 * no + 1, md + 1, hi, pos, newv)
                self.t[no] = max(self.t[2 * no], self.t[2 * no + 1])
            
            def upd(self, pos, newv):
                self._upd(1, 0, self.nn - 1, pos, newv)
            
            def _qry(self, no, lo, hi, ql, qr):
                if qr < lo or hi < ql:
                    return 0
                if ql <= lo and hi <= qr:
                    return self.t[no]
                md = (lo + hi) // 2
                return max(self._qry(2 * no, lo, md, ql, qr),
                           self._qry(2 * no + 1, md + 1, hi, ql, qr))
            
            def qry(self, ql, qr):
                return self._qry(1, 0, self.nn - 1, ql, qr)
        
        tree = MaxSegTree(num) if num > 0 else None
        ordered = SortedList()
        answers = []
        
        for qq in queries:
            tp = qq[0]
            xx = qq[1]
            ins_pt = ordered.bisect_left(xx)
            prv = ordered[ins_pt - 1] if ins_pt > 0 else 0
            if tp == 1:
                ordered.add(xx)
                tree.upd(ranks[xx], xx - prv)
                if ins_pt + 1 < len(ordered):
                    nxtv = ordered[ins_pt + 1]
                    tree.upd(ranks[nxtv], nxtv - xx)
            else:
                req = qq[2]
                curr_gap = xx - prv
                can_place = curr_gap >= req
                if not can_place and ins_pt > 0:
                    prv_rank = ranks[ordered[ins_pt - 1]]
                    can_place = tree.qry(0, prv_rank) >= req
                answers.append(can_place)
        
        return answers
