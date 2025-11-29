import collections

class C1(object):

    def numFriendRequests(self, a1):
        """
        """

        def request(a1, a2):
            return 0.5 * a1 + 7 < a2 <= a1
        v1 = collections.Counter(a1)
        return sum((int(request(a, b)) * v1[a] * (v1[b] - int(a == b)) for v2 in v1 for v3 in v1))
