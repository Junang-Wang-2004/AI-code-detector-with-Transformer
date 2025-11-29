class Solution:
    def findHighAccessEmployees(self, access_times):
        employee_minutes = {}
        for emp_id, time_string in access_times:
            hours = int(time_string[0:2])
            minutes = int(time_string[2:4])
            total_minutes = hours * 60 + minutes
            if emp_id not in employee_minutes:
                employee_minutes[emp_id] = []
            employee_minutes[emp_id].append(total_minutes)
        
        violators = []
        for emp_id, access_list in employee_minutes.items():
            sorted_access = sorted(access_list)
            count = len(sorted_access)
            if count >= 3:
                violation_found = False
                for start in range(count - 2):
                    if sorted_access[start + 2] - sorted_access[start] < 60:
                        violation_found = True
                        break
                if violation_found:
                    violators.append(emp_id)
        return violators
