class Solution:
    def average(self, salary):
        sorted_salaries = sorted(salary)
        return sum(sorted_salaries[1:-1]) / (len(salary) - 2)
