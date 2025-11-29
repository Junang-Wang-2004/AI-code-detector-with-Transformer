from sortedcontainers import SortedList
import collections

class Solution(object):
    def findXSum(self, nums, k, x):
        freq_map = {}
        ord_list = SortedList()
        res = []
        cur_sum = 0

        def increment(val):
            nonlocal cur_sum
            prior = freq_map.get(val, 0)
            next_cnt = prior + 1
            freq_map[val] = next_cnt
            if prior > 0:
                prev_tup = (-prior, -val)
                pos = ord_list.index(prev_tup)
                if pos < x:
                    cur_sum -= prior * val
                if len(ord_list) > x:
                    nf, nv = ord_list[x]
                    cur_sum += (-nf) * (-nv)
                ord_list.remove(prev_tup)
            next_tup = (-next_cnt, -val)
            ord_list.add(next_tup)
            pos = ord_list.index(next_tup)
            if pos < x:
                cur_sum += next_cnt * val
            if len(ord_list) > x:
                nf, nv = ord_list[x]
                cur_sum -= (-nf) * (-nv)

        def decrement(val):
            nonlocal cur_sum
            prior = freq_map[val]
            next_cnt = prior - 1
            freq_map[val] = next_cnt
            prev_tup = (-prior, -val)
            pos = ord_list.index(prev_tup)
            if pos < x:
                cur_sum -= prior * val
            if len(ord_list) > x:
                nf, nv = ord_list[x]
                cur_sum += (-nf) * (-nv)
            ord_list.remove(prev_tup)
            if next_cnt > 0:
                next_tup = (-next_cnt, -val)
                ord_list.add(next_tup)
                pos = ord_list.index(next_tup)
                if pos < x:
                    cur_sum += next_cnt * val
                if len(ord_list) > x:
                    nf, nv = ord_list[x]
                    cur_sum -= (-nf) * (-nv)
            else:
                del freq_map[val]

        n = len(nums)
        for i in range(n):
            increment(nums[i])
            if i >= k - 1:
                res.append(cur_sum)
                leaving = nums[i - k + 1]
                decrement(leaving)
        return res
