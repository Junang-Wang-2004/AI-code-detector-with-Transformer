class Solution:
    def alertNames(self, keyName, keyTime):
        def to_minutes(time_str):
            hours, minutes = time_str.split(':')
            return int(hours) * 60 + int(minutes)
        
        access_times = {}
        for i in range(len(keyName)):
            emp = keyName[i]
            mins = to_minutes(keyTime[i])
            if emp not in access_times:
                access_times[emp] = []
            access_times[emp].append(mins)
        
        suspicious = []
        for emp, logs in access_times.items():
            logs.sort()
            log_count = len(logs)
            has_alert = False
            for start in range(log_count - 2):
                if logs[start + 2] - logs[start] <= 60:
                    has_alert = True
                    break
            if has_alert:
                suspicious.append(emp)
        
        suspicious.sort()
        return suspicious
