class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        extra = money - children
        max_k = extra // 7
        remainder = extra % 7
        if max_k > children:
            max_k = children - 1
        elif max_k == children:
            if remainder != 0:
                max_k -= 1
        elif max_k == children - 1:
            if remainder == 3:
                max_k -= 1
        return max_k
