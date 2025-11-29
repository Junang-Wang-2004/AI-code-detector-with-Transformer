class Solution(object):
    def amountOfTime(self, root, start):
        def locate_start(r):
            if not r:
                return None
            pile = [r]
            while pile:
                curr = pile.pop()
                if curr.val == start:
                    return curr
                if curr.right:
                    pile.append(curr.right)
                if curr.left:
                    pile.append(curr.left)
            return None

        begin = locate_start(root)
        seen = set([begin])
        q = [begin]
        time = 0
        while q:
            nxt = []
            for no in q:
                for nb in (no.left, no.right):
                    if nb and nb not in seen:
                        seen.add(nb)
                        nxt.append(nb)
            q = nxt
            if q:
                time += 1
        return time
