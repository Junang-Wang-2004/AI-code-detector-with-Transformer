import random

class Treap:
    class Node:
        def __init__(self, val):
            self.val = val
            self.prio = random.randrange(1 << 31)
            self.sz = 1
            self.xsum = val
            self.flip = False
            self.lc = None
            self.rc = None

    def __init__(self, arr):
        self.root = self._build(arr, 0, len(arr))

    def _build(self, arr, lo, hi):
        if lo == hi:
            return None
        md = (lo + hi) // 2
        nd = self.Node(arr[md])
        nd.lc = self._build(arr, lo, md)
        nd.rc = self._build(arr, md + 1, hi)
        self._update_node(nd)
        return nd

    def _get_size(self, nd):
        return nd.sz if nd else 0

    def _get_xor(self, nd):
        return nd.xsum if nd else 0

    def _push(self, nd):
        if not nd or not nd.flip:
            return
        nd.flip = False
        nd.lc, nd.rc = nd.rc, nd.lc
        if nd.lc:
            nd.lc.flip = not nd.lc.flip
        if nd.rc:
            nd.rc.flip = not nd.rc.flip

    def _update_node(self, nd):
        if nd:
            nd.sz = 1 + self._get_size(nd.lc) + self._get_size(nd.rc)
            nd.xsum = nd.val ^ self._get_xor(nd.lc) ^ self._get_xor(nd.rc)

    def _split(self, nd, k):
        if nd is None:
            return None, None
        self._push(nd)
        lsz = self._get_size(nd.lc)
        if lsz >= k:
            lft, nd.lc = self._split(nd.lc, k)
            self._update_node(nd)
            return lft, nd
        else:
            nd.rc, rgt = self._split(nd.rc, k - lsz - 1)
            self._update_node(nd)
            return nd, rgt

    def _merge(self, lft, rgt):
        self._push(lft)
        self._push(rgt)
        if lft is None:
            return rgt
        if rgt is None:
            return lft
        if lft.prio > rgt.prio:
            lft.rc = self._merge(lft.rc, rgt)
            self._update_node(lft)
            return lft
        rgt.lc = self._merge(lft, rgt.lc)
        self._update_node(rgt)
        return rgt

    def update(self, pos, val):
        lft, md = self._split(self.root, pos - 1)
        md, rgt = self._split(md, 1)
        if md:
            md.val = val
            self._update_node(md)
        self.root = self._merge(self._merge(lft, md), rgt)

    def query(self, lpos, rpos):
        lft, md = self._split(self.root, lpos - 1)
        md, rgt = self._split(md, rpos - lpos + 1)
        xv = self._get_xor(md)
        self.root = self._merge(self._merge(lft, md), rgt)
        return xv

    def reverse(self, lpos, rpos):
        lft, md = self._split(self.root, lpos - 1)
        md, rgt = self._split(md, rpos - lpos + 1)
        if md:
            md.flip = not md.flip
        self.root = self._merge(self._merge(lft, md), rgt)


class Solution:
    def getResults(self, nums, queries):
        tr = Treap(nums)
        rst = []
        for q in queries:
            tp, li, ri = q
            if tp == 1:
                tr.update(li, ri)
            elif tp == 2:
                rst.append(tr.query(li, ri))
            elif tp == 3:
                tr.reverse(li, ri)
        return rst
