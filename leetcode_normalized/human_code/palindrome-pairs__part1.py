import collections

class C1(object):

    def palindromePairs(self, a1):
        """
        """

        def is_palindrome(a1, a2, a3):
            while a2 < a3:
                if a1[a2] != a1[a3]:
                    return False
                a2 += 1
                a3 -= 1
            return True
        v1 = []
        v2 = collections.defaultdict(dict)
        for v3, v4 in enumerate(a1):
            v2[len(v4)][v4] = v3
        for v3 in range(len(a1)):
            for v5 in range(len(a1[v3]) + 1):
                if v5 in v2 and is_palindrome(a1[v3], v5, len(a1[v3]) - 1):
                    v6 = a1[v3][:v5][::-1]
                    v7 = v2[len(v6)]
                    if v6 in v7 and v7[v6] != v3:
                        v1.append([v3, v7[v6]])
                if v5 > 0 and len(a1[v3]) - v5 in v2 and is_palindrome(a1[v3], 0, v5 - 1):
                    v8 = a1[v3][v5:][::-1]
                    v7 = v2[len(v8)]
                    if v8 in v7 and v7[v8] != v3:
                        v1.append([v7[v8], v3])
        return v1
