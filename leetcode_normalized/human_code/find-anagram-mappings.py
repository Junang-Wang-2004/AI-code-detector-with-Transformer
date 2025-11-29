import collections

class C1(object):

    def anagramMappings(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(collections.deque)
        for v2, v3 in enumerate(a2):
            v1[v3].append(v2)
        v4 = []
        for v3 in a1:
            v4.append(v1[v3].popleft())
        return v4
