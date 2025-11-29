class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        last = -1
        building = 0
        active = False
        for char in s:
            if char.isdigit():
                if not active:
                    active = True
                    building = 0
                building = building * 10 + int(char)
            else:
                if active:
                    if building <= last:
                        return False
                    last = building
                    active = False
        return not active or building > last
