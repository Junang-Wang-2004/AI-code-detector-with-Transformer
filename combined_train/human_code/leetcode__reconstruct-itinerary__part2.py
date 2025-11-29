import collections

class C1(object):

    def findItinerary(self, a1):
        """
        """

        def route_helper(a1, a2, a3, a4):
            if a2 == 0:
                return True
            for v1, (v2, v3) in enumerate(a3[a1]):
                if v3:
                    a3[a1][v1][1] = False
                    a4.append(v2)
                    if route_helper(v2, a2 - 1, a3, a4):
                        return a4
                    a4.pop()
                    a3[a1][v1][1] = True
            return False
        v1 = collections.defaultdict(list)
        for v2 in a1:
            v1[v2[0]].append([v2[1], True])
        for v3 in list(v1.keys()):
            v1[v3].sort()
        v4 = 'JFK'
        v5 = [v4]
        route_helper(v4, len(a1), v1, v5)
        return v5
