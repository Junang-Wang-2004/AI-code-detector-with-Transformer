class Solution:
    def longestDiverseString(self, aa, bb, cc):
        cnt = [aa, bb, cc]
        ch = 'abc'
        ans = []
        while True:
            idx = -1
            mx = -1
            for i in range(3):
                if cnt[i] > 0:
                    if len(ans) < 2 or not (ans[-1] == ans[-2] == ch[i]):
                        if cnt[i] > mx:
                            mx = cnt[i]
                            idx = i
            if idx == -1:
                break
            ans.append(ch[idx])
            cnt[idx] -= 1
        return ''.join(ans)
