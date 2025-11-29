class Solution(object):
    def totalReplacements(self, ranks):
        record_mins = []
        for val in ranks:
            if not record_mins or val < record_mins[-1]:
                record_mins.append(val)
        return len(record_mins) - 1
