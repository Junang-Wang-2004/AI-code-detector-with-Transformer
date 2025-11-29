class Solution(object):
    def scoreOfStudents(self, s, answers):
        nums = [int(s[i]) for i in range(0, len(s), 2)]
        ops = [s[i] for i in range(1, len(s), 2)]
        m = len(nums)
        MAX_VAL = 1000
        poss = [[set() for _ in range(m)] for _ in range(m)]
        for i in range(m):
            poss[i][i].add(nums[i])
        for leng in range(2, m + 1):
            for i in range(m - leng + 1):
                j = i + leng - 1
                for k in range(i, j):
                    op = ops[k]
                    left_vals = poss[i][k]
                    right_vals = poss[k + 1][j]
                    if op == '+':
                        for x in left_vals:
                            for y in right_vals:
                                sm = x + y
                                if sm <= MAX_VAL:
                                    poss[i][j].add(sm)
                    else:
                        for x in left_vals:
                            for y in right_vals:
                                prod = x * y
                                if prod <= MAX_VAL:
                                    poss[i][j].add(prod)
        all_poss = poss[0][m - 1]
        terms = []
        curr = nums[0]
        for idx in range(len(ops)):
            if ops[idx] == '*':
                curr *= nums[idx + 1]
            else:
                terms.append(curr)
                curr = nums[idx + 1]
        terms.append(curr)
        target = sum(terms)
        return sum(5 if a == target else 2 if a in all_poss else 0 for a in answers)
