class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def get_rev(val: int) -> int:
            reversed_num = 0
            place_value = 1
            temp_val = val
            while temp_val > 0:
                last_digit = temp_val % 10
                reversed_num += last_digit * place_value
                place_value *= 10
                temp_val //= 10
            return reversed_num

        low = num // 2
        for possible_x in range(low, num + 1):
            if possible_x + get_rev(possible_x) == num:
                return True
        return False
