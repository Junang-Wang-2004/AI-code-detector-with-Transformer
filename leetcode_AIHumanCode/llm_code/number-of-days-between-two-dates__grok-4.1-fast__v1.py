class Solution:
    def daysBetweenDates(self, first_date, second_date):
        month_len = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def total_days_up_to(date_str):
            yr = int(date_str[0:4])
            mo = int(date_str[5:7])
            dy = int(date_str[8:10])
            
            yrs_days = (yr - 1) * 365 + (yr - 1) // 4 - (yr - 1) // 100 + (yr - 1) // 400
            
            mos_days = sum(month_len[i] for i in range(1, mo))
            
            if mo > 2 and (yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0)):
                mos_days += 1
            
            return yrs_days + mos_days + dy
        
        return abs(total_days_up_to(first_date) - total_days_up_to(second_date))
