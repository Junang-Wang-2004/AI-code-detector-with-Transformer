from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        run_lengths = defaultdict(list)
        i = 0
        n = len(s)
        while i < n:
            start = i
            while i < n and s[i] == s[start]:
                i += 1
            run_lengths[ord(s[start]) - ord('a')].append(i - start)
        answer = 0
        for lengths in run_lengths.values():
            if lengths:
                sorted_lengths = sorted(lengths, reverse=True)
                first = sorted_lengths[0]
                second = sorted_lengths[1] if len(sorted_lengths) > 1 else 0
                third = sorted_lengths[2] if len(sorted_lengths) > 2 else 0
                option1 = first - 2
                option2 = min(first - 1, second)
                option3 = third
                answer = max(answer, option1, option2, option3)
        return answer if answer > 0 else -1
