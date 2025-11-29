# Time:  O(s * t)
# Space: O(s)

class Solution(object):
    def minWindow(self, S, T):
        """
        """
        lookup = [[None for _ in range(26)] for _ in range(len(S)+1)]
        find_char_next_pos = [None]*26
        for i in reversed(range(len(S))):
            find_char_next_pos[ord(S[i])-ord('a')] = i+1
            lookup[i] = list(find_char_next_pos)

        min_i, min_len = None, float("inf")
        for i in range(len(S)):
            if S[i] != T[0]:
                continue
            start = i
            for c in T:
                start = lookup[start][ord(c)-ord('a')]
                if start == None:
                    break
            else:
                if start-i < min_len:
                    min_i, min_len = i, start-i
        return S[min_i:min_i+min_len] if min_i is not None else ""

    
