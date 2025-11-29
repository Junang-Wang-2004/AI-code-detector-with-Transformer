import collections
import bisect

class WordDistance(object):
    def __init__(self, words):
        self.pos = collections.defaultdict(list)
        for idx, term in enumerate(words):
            self.pos[term].append(idx)

    def shortest(self, term1, term2):
        lista = self.pos[term1]
        listb = self.pos[term2]
        if len(lista) > len(listb):
            lista, listb = listb, lista
        mind = float('inf')
        for val in lista:
            it = bisect.bisect_left(listb, val)
            if it < len(listb):
                mind = min(mind, listb[it] - val)
            if it > 0:
                mind = min(mind, val - listb[it - 1])
        return mind
