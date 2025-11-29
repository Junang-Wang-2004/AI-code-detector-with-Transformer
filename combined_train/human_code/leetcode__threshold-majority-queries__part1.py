class C1(object):

    def subarrayMajority(self, a1, a2):
        """
        """

        def mo_s_algorithm():

            def add(a1):
                v1 = num_to_idx[a1[a1]]
                if cnt[v1]:
                    cnt2[cnt[v1]] -= 1
                cnt[v1] += 1
                cnt2[cnt[v1]] += 1
                max_freq[0] = max(max_freq[0], cnt[v1])

            def remove(a1):
                v1 = num_to_idx[a1[a1]]
                cnt2[cnt[v1]] -= 1
                if not cnt2[max_freq[0]]:
                    max_freq[0] -= 1
                cnt[v1] -= 1
                if cnt[v1]:
                    cnt2[cnt[v1]] += 1

            def get_ans(a1):
                if max_freq[0] < a1:
                    return -1
                v1 = next((v1 for v1 in range(len(cnt)) if cnt[v1] == max_freq[0]))
                return sorted_nums[v1]
            v1 = [0] * len(num_to_idx)
            v2 = [0] * (len(a1) + 1)
            v3 = [0]
            v4 = [-1] * len(a2)
            v5 = int(len(a1) ** 0.5) + 1
            v6 = list(range(len(a2)))
            v6.sort(key=lambda x: (a2[x][0] // v5, a2[x][1] if a2[x][0] // v5 & 1 else -a2[x][1]))
            v7, v8 = (0, -1)
            for v9 in v6:
                v10, v11, v12 = a2[v9]
                while v7 > v10:
                    v7 -= 1
                    add(v7)
                while v8 < v11:
                    v8 += 1
                    add(v8)
                while v7 < v10:
                    remove(v7)
                    v7 += 1
                while v8 > v11:
                    remove(v8)
                    v8 -= 1
                v4[v9] = get_ans(v12)
            return v4
        v1 = sorted(set(a1))
        v2 = {x: i for v3, v4 in enumerate(v1)}
        return mo_s_algorithm()
