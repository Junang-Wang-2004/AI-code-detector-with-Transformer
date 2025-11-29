class Solution:
    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        ones_dict = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
        }
        teens_dict = {
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
        }
        tens_dict = {
            2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty",
            7: "Seventy", 8: "Eighty", 9: "Ninety"
        }
        group_names = ["Billion", "Million", "Thousand", ""]
        divisors = [10**9, 10**6, 10**3, 1]

        result_parts = []
        for idx, divisor in enumerate(divisors):
            group = (num // divisor) % 1000
            if group > 0:
                group_str = self._convert_group(group, ones_dict, teens_dict, tens_dict)
                if group_names[idx]:
                    group_str += " " + group_names[idx]
                result_parts.append(group_str)

        return " ".join(result_parts)

    def _convert_group(self, n, ones, teens, tens):
        parts = []
        hundreds = n // 100
        remainder = n % 100
        if hundreds > 0:
            parts.append(ones[hundreds] + " Hundred")
        if remainder > 0:
            if remainder < 10:
                parts.append(ones[remainder])
            elif remainder < 20:
                parts.append(teens[remainder])
            else:
                ten = remainder // 10
                one = remainder % 10
                parts.append(tens[ten])
                if one > 0:
                    parts.append(ones[one])
        return " ".join(parts)
