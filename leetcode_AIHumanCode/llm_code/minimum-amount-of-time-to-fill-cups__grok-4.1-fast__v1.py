class Solution:
    def fillCups(self, amount):
        nums = sorted(amount, reverse=True)
        top, mid, bot = nums
        total = top + mid + bot
        if top > mid + bot:
            return top
        return (total + 1) // 2
