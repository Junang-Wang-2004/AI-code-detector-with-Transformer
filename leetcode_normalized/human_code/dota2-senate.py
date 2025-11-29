import collections

class C1(object):

    def predictPartyVictory(self, a1):
        """
        """
        v1 = len(a1)
        v2, v3 = (collections.deque(), collections.deque())
        for v4, v5 in enumerate(a1):
            if v5 == 'R':
                v2.append(v4)
            else:
                v3.append(v4)
        while v2 and v3:
            v6, v7 = (v2.popleft(), v3.popleft())
            if v6 < v7:
                v2.append(v6 + v1)
            else:
                v3.append(v7 + v1)
        return 'Radiant' if len(v2) > len(v3) else 'Dire'
