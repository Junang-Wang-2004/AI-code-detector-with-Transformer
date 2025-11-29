# Time:  O(n), n is the length of sequence
# Space: O(n)
# kmp solution
class Solution2(object):
    def maxRepeating(self, sequence, word):
        """
        """
        def getPrefix(pattern):
            prefix = [-1] * len(pattern)
            j = -1
            for i in range(1, len(pattern)):
                while j > -1 and pattern[j + 1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix

        if len(sequence) < len(word):
            return 0

        new_word = word*(len(sequence)//len(word))
        prefix = getPrefix(new_word)
        result, j = 0, -1
        for i in range(len(sequence)):
            while j > -1 and new_word[j+1] != sequence[i]:
                j = prefix[j]
            if new_word[j+1] == sequence[i]:
                j += 1
            result = max(result, j+1)
            if j+1 == len(new_word):     
                break
        return result//len(word)
