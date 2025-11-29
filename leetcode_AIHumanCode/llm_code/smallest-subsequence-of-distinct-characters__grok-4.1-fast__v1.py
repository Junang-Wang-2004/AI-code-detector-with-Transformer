class Solution:
    def smallestSubsequence(self, text):
        length = len(text)
        final_pos = {}
        for j in range(length):
            final_pos[text[j]] = j
        pile = []
        tracked = set()
        for k in range(length):
            ch = text[k]
            if ch not in tracked:
                while pile and pile[-1] > ch and final_pos[pile[-1]] > k:
                    tracked.remove(pile.pop())
                pile.append(ch)
                tracked.add(ch)
        return "".join(pile)
