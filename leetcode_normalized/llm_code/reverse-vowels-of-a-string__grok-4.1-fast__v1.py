class C1:

    def reverseVowels(self, a1):
        v1 = set('aeiouAEIOU')
        v2 = list(a1)
        v3 = []
        for v4 in a1:
            if v4 in v1:
                v3.append(v4)
        v3.reverse()
        v5 = 0
        for v6 in range(len(v2)):
            if v2[v6] in v1:
                v2[v6] = v3[v5]
                v5 += 1
        return ''.join(v2)
