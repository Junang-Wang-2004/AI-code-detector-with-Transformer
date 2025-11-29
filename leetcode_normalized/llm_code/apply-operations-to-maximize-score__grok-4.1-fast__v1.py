class C1(object):

    def maximumScore(self, a1, a2):
        v1 = 10 ** 9 + 7

        def generate_primes(a1):
            if a1 < 2:
                return []
            v1 = [True] * (a1 + 1)
            v1[0] = v1[1] = False
            for v2 in range(2, int(a1 ** 0.5) + 1):
                if v1[v2]:
                    for v3 in range(v2 * v2, a1 + 1, v2):
                        v1[v3] = False
            return [v2 for v2 in range(a1 + 1) if v1[v2]]
        v2 = max(a1)
        v3 = int(v2 ** 0.5) + 1
        v4 = generate_primes(v3)
        v5 = {}

        def distinct_prime_count(a1):
            if a1 in v5:
                return v5[a1]
            v1 = a1
            v2 = 0
            for v3 in v4:
                if v3 * v3 > v1:
                    break
                if v1 % v3 == 0:
                    v2 += 1
                    while v1 % v3 == 0:
                        v1 //= v3
            if v1 > 1:
                v2 += 1
            v5[a1] = v2
            return v2
        v6 = [distinct_prime_count(x) for v7 in a1]
        v8 = len(a1)
        v9 = [-1] * v8
        v10 = [-1]
        for v11 in range(v8):
            while v10[-1] != -1 and v6[v10[-1]] < v6[v11]:
                v10.pop()
            v9[v11] = v10[-1]
            v10.append(v11)
        v12 = [v8] * v8
        v13 = [v8]
        for v11 in range(v8 - 1, -1, -1):
            while v13[-1] != v8 and v6[v13[-1]] <= v6[v11]:
                v13.pop()
            v12[v11] = v13[-1]
            v13.append(v11)
        v14 = []
        for v11 in range(v8):
            v15 = v11 - v9[v11]
            v16 = v12[v11] - v11
            v14.append(v15 * v16)
        v17 = [(a1[v11], v14[v11]) for v11 in range(v8)]
        v17.sort(reverse=True)
        v18 = 1
        v19 = a2
        for v20, v21 in v17:
            if v19 <= 0:
                break
            v22 = min(v21, v19)
            v18 = v18 * pow(v20, v22, v1) % v1
            v19 -= v22
        return v18
