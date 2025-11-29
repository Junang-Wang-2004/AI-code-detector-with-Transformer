class Solution:
    def numOfPairs(self, nums, target):
        pre_freq = {}
        suf_freq = {}
        pair_count = 0
        tlen = len(target)
        for digit_str in nums:
            slen = len(digit_str)
            need_len = tlen - slen
            is_pre = digit_str == target[:slen]
            is_suf = digit_str == target[-slen:]
            if is_pre:
                pair_count += suf_freq.get(need_len, 0)
            if is_suf:
                pair_count += pre_freq.get(need_len, 0)
            if is_pre:
                pre_freq[slen] = pre_freq.get(slen, 0) + 1
            if is_suf:
                suf_freq[slen] = suf_freq.get(slen, 0) + 1
        return pair_count
