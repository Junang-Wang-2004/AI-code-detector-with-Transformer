class Solution:
    def numSplits(self, s):
        offset = ord('a')
        lfreq = [0] * 26
        rfreq = [0] * 26
        for ch in s:
            rfreq[ord(ch) - offset] += 1
        runiq = sum(1 for x in rfreq if x > 0)
        luniq = 0
        ways = 0
        for ch in s:
            i = ord(ch) - offset
            lfreq[i] += 1
            if lfreq[i] == 1:
                luniq += 1
            rfreq[i] -= 1
            if rfreq[i] == 0:
                runiq -= 1
            if luniq == runiq:
                ways += 1
        return ways
