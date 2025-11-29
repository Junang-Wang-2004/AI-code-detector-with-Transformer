class Solution:
    def wordsTyping(self, paragraph: List[str], rows: int, cols: int) -> int:
        n = len(paragraph)
        wlen = [len(w) for w in paragraph]
        
        def fit_from(pos: int) -> int:
            if wlen[pos] > cols:
                return 0
            rem = cols - wlen[pos]
            cnt = 1
            nxt = (pos + 1) % n
            while rem >= 1 + wlen[nxt]:
                rem -= 1 + wlen[nxt]
                cnt += 1
                nxt = (nxt + 1) % n
            return cnt
        
        step = [fit_from(i) for i in range(n)]
        tot = 0
        cur = 0
        for _ in range(rows):
            tot += step[cur]
            cur = (cur + step[cur]) % n
        return tot // n
