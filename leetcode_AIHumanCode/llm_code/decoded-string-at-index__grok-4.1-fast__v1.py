class Solution(object):
    def decodeAtIndex(self, S, K):
        length = 0
        for char in S:
            if char.isdigit():
                length *= int(char)
            else:
                length += 1
        target = K
        position = len(S) - 1
        while position >= 0:
            char = S[position]
            target %= length
            if target == 0 and char.isalpha():
                return char
            if char.isdigit():
                length //= int(char)
            else:
                length -= 1
            position -= 1
