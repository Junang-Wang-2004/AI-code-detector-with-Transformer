class Solution:
    def intersect(self, list_a, list_b):
        if len(list_a) > len(list_b):
            list_a, list_b = list_b, list_a
        freq = {}
        for val in list_a:
            if val not in freq:
                freq[val] = 0
            freq[val] += 1
        output = []
        for val in list_b:
            if val in freq and freq[val] > 0:
                output.append(val)
                freq[val] -= 1
        return output
