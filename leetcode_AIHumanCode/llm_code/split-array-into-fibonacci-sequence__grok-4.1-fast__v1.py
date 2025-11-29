class Solution:
    def splitIntoFibonacci(self, S):
        n = len(S)
        MAX_VAL = (1 << 31) - 1

        def helper(pos, p1, p2, path):
            if pos == n:
                return len(path) >= 3
            next_val = p1 + p2
            if next_val > MAX_VAL:
                return False
            next_str = str(next_val)
            next_len = len(next_str)
            if pos + next_len > n or S[pos:pos + next_len] != next_str:
                return False
            path.append(next_val)
            if helper(pos + next_len, p2, next_val, path):
                return True
            path.pop()
            return False

        for end1 in range(1, min(n, 11)):
            if S[0] == '0' and end1 > 1:
                continue
            num1 = int(S[:end1])
            if num1 > MAX_VAL:
                break
            for end2 in range(end1 + 1, min(n + 1, end1 + 11)):
                if S[end1] == '0' and end2 - end1 > 1:
                    continue
                num2 = int(S[end1:end2])
                if num2 > MAX_VAL:
                    break
                path = [num1, num2]
                if helper(end2, num1, num2, path):
                    return path
        return []
