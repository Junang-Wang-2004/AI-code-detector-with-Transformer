from sortedcontainers import SortedList

class C1(object):

    def subarrayMajority(self, a1, a2):
        """
        """

        def mo_s_algorithm():

            def add(a1):
                v1 = num_to_idx[a1[a1]]
                if cnt[v1]:
                    lookup[cnt[v1]].remove(a1[a1])
                cnt[v1] += 1
                lookup[cnt[v1]].add(a1[a1])
                max_freq[0] = max(max_freq[0], cnt[v1])

            def remove(a1):
                v1 = num_to_idx[a1[a1]]
                lookup[cnt[v1]].remove(a1[a1])
                if not lookup[max_freq[0]]:
                    max_freq[0] -= 1
                cnt[v1] -= 1
                if cnt[v1]:
                    lookup[cnt[v1]].add(a1[a1])

            def get_ans(a1):
                return lookup[max_freq[0]][0] if max_freq[0] >= a1 else -1
            v1 = [0] * len(num_to_idx)
            v2 = [SortedList() for v3 in range(len(a1) + 1)]
            v4 = [0]
            v5 = [-1] * len(a2)
            v6 = int(len(a1) ** 0.5) + 1
            v7 = list(range(len(a2)))
            v7.sort(key=lambda x: (a2[x][0] // v6, a2[x][1] if a2[x][0] // v6 & 1 else -a2[x][1]))
            v8, v9 = (0, -1)
            for v10 in v7:
                v11, v12, v13 = a2[v10]
                while v8 > v11:
                    v8 -= 1
                    add(v8)
                while v9 < v12:
                    v9 += 1
                    add(v9)
                while v8 < v11:
                    remove(v8)
                    v8 += 1
                while v9 > v12:
                    remove(v9)
                    v9 -= 1
                v5[v10] = get_ans(v13)
            return v5
        v1 = {x: i for v2, v3 in enumerate(sorted(set(a1)))}
        return mo_s_algorithm()
