class C1(object):

    def bestHand(self, a1, a2):
        """
        """
        v1 = ['', 'High Card', 'Pair', 'Three of a Kind', 'Three of a Kind', 'Three of a Kind']
        if all((a2[i] == a2[0] for v2 in range(1, len(a2)))):
            return 'Flush'
        v3 = [0] * 13
        for v4 in a1:
            v3[v4 - 1] += 1
        return v1[max(v3)]
