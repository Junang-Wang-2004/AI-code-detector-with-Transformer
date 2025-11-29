class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus_pos = expression.index('+')
        pre_plus = expression[:plus_pos]
        post_plus = expression[plus_pos + 1:]
        len_pre = len(pre_plus)
        len_post = len(post_plus)
        min_value = float('inf')
        best_start = 0
        best_end = 0
        for pref_len in range(len_pre):
            pref_a = pre_plus[:pref_len]
            mid_b = pre_plus[pref_len:]
            num_a = int(pref_a) if pref_len > 0 else 1
            num_b = int(mid_b)
            for post_len in range(1, len_post + 1):
                mid_c = post_post[:post_len]
                suf_d = post_plus[post_len:]
                num_c = int(mid_c)
                num_d = int(suf_d) if post_len < len_post else 1
                current = num_a * (num_b + num_c) * num_d
                if current < min_value:
                    min_value = current
                    best_start = pref_len
                    best_end = plus_pos + post_len
        return (expression[:best_start] + '(' + expression[best_start:best_end + 1] +
                ')' + expression[best_end + 1:])
