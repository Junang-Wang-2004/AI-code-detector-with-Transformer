class Solution(object):
    def compareVersion(self, version1, version2):
        chunks1 = list(map(int, version1.split('.')))
        chunks2 = list(map(int, version2.split('.')))
        idx = 0
        while idx < len(chunks1) or idx < len(chunks2):
            num1 = chunks1[idx] if idx < len(chunks1) else 0
            num2 = chunks2[idx] if idx < len(chunks2) else 0
            if num1 < num2:
                return -1
            if num1 > num2:
                return 1
            idx += 1
        return 0
