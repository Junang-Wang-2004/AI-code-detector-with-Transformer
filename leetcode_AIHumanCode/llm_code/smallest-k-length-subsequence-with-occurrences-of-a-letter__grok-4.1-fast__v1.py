class Solution:
    def smallestSubsequence(self, s, k, letter, repetition):
        n = len(s)
        avail = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            avail[i] = avail[i + 1] + (s[i] == letter)
        mono = []
        remain = repetition
        for j, ch in enumerate(s):
            while mono and mono[-1] > ch and len(mono) + n - j > k and \
                  (mono[-1] != letter or remain + 1 <= avail[j]):
                if mono.pop() == letter:
                    remain += 1
            delta = 1 if ch == letter else 0
            if len(mono) < k - (remain - delta):
                if delta:
                    remain -= 1
                mono.append(ch)
        return "".join(mono)
