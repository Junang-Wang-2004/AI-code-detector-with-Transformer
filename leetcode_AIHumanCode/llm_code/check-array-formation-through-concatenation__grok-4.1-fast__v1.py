class Solution:
    def canFormArray(self, arr, pieces):
        idx = 0
        while idx < len(arr):
            matched = False
            for segment in pieces:
                seg_len = len(segment)
                if idx + seg_len <= len(arr) and arr[idx:idx + seg_len] == segment:
                    idx += seg_len
                    matched = True
                    break
            if not matched:
                return False
        return True
