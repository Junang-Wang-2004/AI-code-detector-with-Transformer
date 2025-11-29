class Solution:
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        idx_sorted = sorted(range(len(values)), key=lambda x: values[x], reverse=True)
        track = {}
        sum_val = 0
        left = num_wanted
        for pos in idx_sorted:
            tag = labels[pos]
            score = values[pos]
            prev = track.get(tag, 0)
            if prev < use_limit and left > 0:
                sum_val += score
                track[tag] = prev + 1
                left -= 1
        return sum_val
