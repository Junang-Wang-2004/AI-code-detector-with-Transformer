class Solution:
    def shortestMatchingSubstring(self, s, p):
        parts = p.split('*')
        pre, mid, suf = parts
        lp = len(pre)
        lm = len(mid)
        ls = len(suf)
        n = len(s)

        def compute_lps(pat):
            m = len(pat)
            lps = [0] * m
            length = 0
            i = 1
            while i < m:
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        def get_match_starts(txt, pat):
            nn = len(txt)
            if len(pat) == 0:
                return list(range(nn + 1))
            lps = compute_lps(pat)
            matches = []
            j = 0
            for i in range(nn):
                while j > 0 and pat[j] != txt[i]:
                    j = lps[j - 1]
                if pat[j] == txt[i]:
                    j += 1
                if j == len(pat):
                    matches.append(i - len(pat) + 1)
                    j = lps[j - 1]
            return matches

        pos_pre = get_match_starts(s, pre)
        pos_mid = get_match_starts(s, mid)
        pos_suf = get_match_starts(s, suf)

        ans = float('inf')
        j = 0
        k = 0
        m_pre = len(pos_pre)
        m_mid = len(pos_mid)
        m_suf = len(pos_suf)
        for idx in range(m_pre):
            start_pre = pos_pre[idx]
            req_b = start_pre + lp
            while j < m_mid and pos_mid[j] < req_b:
                j += 1
            if j >= m_mid:
                break
            start_m = pos_mid[j]
            req_c = start_m + lm
            while k < m_suf and pos_suf[k] < req_c:
                k += 1
            if k >= m_suf:
                break
            start_s = pos_suf[k]
            end_s = start_s + ls - 1
            length = end_s - start_pre + 1
            if length < ans:
                ans = length
        return ans if ans != float('inf') else -1
