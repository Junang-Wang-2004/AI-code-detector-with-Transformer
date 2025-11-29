class Solution(object):
    def maximumEvenSplit(self, total):
        if total % 2 != 0:
            return []
        count = 0
        while count * (count + 1) <= total:
            count += 1
        count -= 1
        if count == 0:
            return []
        res = []
        accum = 0
        for idx in range(1, count):
            num = 2 * idx
            res.append(num)
            accum += num
        last_num = total - accum
        res.append(last_num)
        return res
