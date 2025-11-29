class Solution(object):
    def splitMessage(self, message, limit):
        n = len(message)
        parts_num = 0
        max_digits = 0
        digits_sum = 0
        while True:
            parts_num += 1
            curr_digits = len(str(parts_num))
            if curr_digits > max_digits:
                max_digits = curr_digits
            digits_sum += curr_digits
            est_total = n + digits_sum + parts_num * (3 + max_digits)
            if est_total <= parts_num * limit:
                break
            if 3 + 2 * max_digits >= limit:
                return []
        if 3 + 2 * max_digits >= limit:
            return []
        result = []
        cur_pos = 0
        for seq in range(1, parts_num + 1):
            seq_len = len(str(seq))
            tot_len = max_digits
            seg_len = limit - 3 - seq_len - tot_len
            seg = message[cur_pos:cur_pos + seg_len]
            result.append(seg + "<" + str(seq) + "/" + str(parts_num) + ">")
            cur_pos += seg_len
        return result
