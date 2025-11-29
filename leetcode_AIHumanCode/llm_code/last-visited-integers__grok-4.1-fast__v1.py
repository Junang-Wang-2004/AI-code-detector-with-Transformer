class Solution:
    def lastVisitedIntegers(self, words):
        nums = []
        pointer = -1
        answers = []
        for entry in words:
            if entry == "prev":
                if pointer >= 0:
                    answers.append(nums[pointer])
                else:
                    answers.append(-1)
                pointer -= 1
            else:
                nums.append(int(entry))
                pointer = len(nums) - 1
        return answers
