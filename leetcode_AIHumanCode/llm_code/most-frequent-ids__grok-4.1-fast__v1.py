class Solution:
    def mostFrequentIDs(self, nums, freq):
        freq_map = {}
        highest = 0
        answers = []
        for num, delta in zip(nums, freq):
            prev = freq_map.get(num, 0)
            freq_map[num] = prev + delta
            if freq_map[num] > highest:
                highest = freq_map[num]
            answers.append(highest)
        return answers
