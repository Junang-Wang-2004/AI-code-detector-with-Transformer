class Solution:
    def numRescueBoats(self, people, limit):
        people.sort(reverse=True)
        count = 0
        i = 0
        j = len(people) - 1
        while i <= j:
            count += 1
            if people[i] + people[j] <= limit and i < j:
                i += 1
                j -= 1
            else:
                i += 1
        return count
