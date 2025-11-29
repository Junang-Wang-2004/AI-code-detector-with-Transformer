import random

class Solution:
    def __init__(self, arr):
        self.source = arr

    def reset(self):
        return self.source

    def shuffle(self):
        copy_arr = self.source[:]
        random.shuffle(copy_arr)
        return copy_arr
