import collections

class Solution(object):
    def supersequences(self, words):
        chars = sorted(set(c for w in words for c in w))
        k = len(chars)
        if k == 0:
            return [[0] * 26]
        idmap = {chars[i]: i for i in range(k)}
        graph = [[] for _ in range(k)]
        incoming = [0] * k
        for w in words:
            ui = idmap[w[0]]
            vi = idmap[w[1]]
            graph[ui].append(vi)
            incoming[vi] += 1
        minsize = float('inf')
        goods = []
        for state in range(1 << k):
            multiplicity = [1 + ((state >> j) & 1) for j in range(k)]
            cursize = sum(multiplicity)
            if cursize > minsize:
                continue
            dupes = multiplicity[:]
            dups_in = incoming[:]
            marked = [False] * k
            q = collections.deque()
            for node in range(k):
                if dups_in[node] == 0 or dupes[node] == 2:
                    dupes[node] -= 1
                    marked[node] = True
                    q.append(node)
            while q:
                nextq = collections.deque()
                for node in q:
                    for neigh in graph[node]:
                        dups_in[neigh] -= 1
                        if dups_in[neigh] == 0:
                            dupes[neigh] -= 1
                            if marked[neigh]:
                                continue
                            marked[neigh] = True
                            nextq.append(neigh)
                q = nextq
            if all(x == 0 for x in dupes):
                if cursize < minsize:
                    minsize = cursize
                    goods = [multiplicity[:]]
                elif cursize == minsize:
                    goods.append(multiplicity[:])
        out = []
        a = ord('a')
        for mult in goods:
            profile = [0] * 26
            for j in range(k):
                profile[ord(chars[j]) - a] = mult[j]
            out.append(profile)
        return out
