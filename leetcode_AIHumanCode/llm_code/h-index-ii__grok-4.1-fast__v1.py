class Solution:
    def hIndex(self, citations):
        size = len(citations)
        begin, end = 0, size
        while begin < end:
            pivot = begin + (end - begin + 1) // 2
            if citations[size - pivot] >= pivot:
                begin = pivot
            else:
                end = pivot - 1
        return begin
