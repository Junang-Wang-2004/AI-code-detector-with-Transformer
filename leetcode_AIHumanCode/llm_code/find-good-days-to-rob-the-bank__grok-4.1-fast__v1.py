class Solution(object):
    def goodDaysToRobBank(self, security, time):
        n = len(security)
        prefix = [0] * n
        for j in range(1, n):
            prefix[j] = prefix[j - 1] + 1 if security[j - 1] >= security[j] else 0
        suffix = [0] * n
        for j in range(n - 2, -1, -1):
            suffix[j] = suffix[j + 1] + 1 if security[j] <= security[j + 1] else 0
        output = []
        for j in range(n):
            if prefix[j] >= time and suffix[j] >= time:
                output.append(j)
        return output
