class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        def window_majority(target):
            wrongs = 0
            start = 0
            length = 0
            for end in range(len(answerKey)):
                if answerKey[end] != target:
                    wrongs += 1
                while wrongs > k and start <= end:
                    if answerKey[start] != target:
                        wrongs -= 1
                    start += 1
                length = max(length, end - start + 1)
            return length

        return max(window_majority('T'), window_majority('F'))
