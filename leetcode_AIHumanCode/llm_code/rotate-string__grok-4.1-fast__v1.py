class Solution:
    def rotateString(self, source, target):
        length = len(source)
        if length != len(target):
            return False
        for offset in range(length):
            rotated_match = True
            for pos in range(length):
                if source[(offset + pos) % length] != target[pos]:
                    rotated_match = False
                    break
            if rotated_match:
                return True
        return False
