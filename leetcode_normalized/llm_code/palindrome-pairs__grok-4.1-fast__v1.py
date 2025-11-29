from collections import defaultdict

class C1:

    def palindromePairs(self, a1):
        v1 = defaultdict(list)
        for v2, v3 in enumerate(a1):
            v1[v3].append(v2)

        def check_palindrome(a1):
            v1, v2 = (0, len(a1) - 1)
            while v1 < v2:
                if a1[v1] != a1[v2]:
                    return False
                v1 += 1
                v2 -= 1
            return True
        v4 = []
        for v5 in range(len(a1)):
            v6 = a1[v5]
            v7 = len(v6)
            for v8 in range(v7 + 1):
                v9 = v6[:v8]
                v10 = v6[v8:]
                if check_palindrome(v10):
                    v11 = v9[::-1]
                    for v12 in v1[v11]:
                        if v12 != v5:
                            v4.append([v5, v12])
            for v8 in range(1, v7 + 1):
                v9 = v6[:v8]
                v10 = v6[v8:]
                if check_palindrome(v9):
                    v13 = v10[::-1]
                    for v12 in v1[v13]:
                        if v12 != v5:
                            v4.append([v12, v5])
        return v4
