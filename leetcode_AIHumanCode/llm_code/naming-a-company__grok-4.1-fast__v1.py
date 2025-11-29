class Solution(object):
    def distinctNames(self, ideas):
        groups = [set() for _ in range(26)]
        for word in ideas:
            idx = ord(word[0]) - ord('a')
            groups[idx].add(word[1:])
        total = 0
        for i in range(26):
            for j in range(26):
                if i == j:
                    continue
                common = len(groups[i] & groups[j])
                unique_i = len(groups[i]) - common
                unique_j = len(groups[j]) - common
                total += unique_i * unique_j
        return total
