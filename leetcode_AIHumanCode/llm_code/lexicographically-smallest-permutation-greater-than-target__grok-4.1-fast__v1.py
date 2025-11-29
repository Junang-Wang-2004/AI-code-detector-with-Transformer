class Solution(object):
    def lexGreaterPermutation(self, s, target):
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        aux_freq = freq[:]
        length = len(target)
        diverge_pos = -1
        for idx in range(length):
            char_code = ord(target[idx]) - ord('a')
            if aux_freq[char_code] == 0:
                break
            has_successor = any(aux_freq[k] > 0 for k in range(char_code + 1, 26))
            if has_successor:
                diverge_pos = idx
            aux_freq[char_code] -= 1
        if diverge_pos == -1:
            return ""
        output = []
        for idx in range(diverge_pos):
            output.append(target[idx])
            freq[ord(target[idx]) - ord('a')] -= 1
        pivot_code = ord(target[diverge_pos]) - ord('a')
        successor = None
        for k in range(pivot_code + 1, 26):
            if freq[k] > 0:
                successor = chr(ord('a') + k)
                break
        output.append(successor)
        freq[ord(successor) - ord('a')] -= 1
        for k in range(26):
            output.extend([chr(ord('a') + k)] * freq[k])
        return ''.join(output)
