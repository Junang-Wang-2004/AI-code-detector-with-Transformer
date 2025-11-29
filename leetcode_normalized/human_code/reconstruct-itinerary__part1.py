import collections

class C1(object):

    def findItinerary(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        for v2 in a1:
            v1[v2[0]].append(v2[1])
        for v3 in v1.values():
            v3.sort(reverse=True)
        v4 = 'JFK'
        v5 = []
        v6 = [v4]
        while v6:
            while v1[v6[-1]]:
                v6.append(v1[v6[-1]].pop())
            v5.append(v6.pop())
        v5.reverse()
        return v5
