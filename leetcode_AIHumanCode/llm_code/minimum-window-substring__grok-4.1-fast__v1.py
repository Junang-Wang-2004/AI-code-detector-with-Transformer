from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        required = defaultdict(int)
        for char in t:
            required[char] += 1
        total_needed = len(t)
        window_count = defaultdict(int)
        satisfied = 0
        left = 0
        min_length = float('inf')
        result_start = 0
        for right in range(len(s)):
            window_count[s[right]] += 1
            if s[right] in required and window_count[s[right]] <= required[s[right]]:
                satisfied += 1
            while satisfied == total_needed and left <= right:
                current_length = right - left + 1
                if current_length < min_length:
                    min_length = current_length
                    result_start = left
                window_count[s[left]] -= 1
                if s[left] in required and window_count[s[left]] < required[s[left]]:
                    satisfied -= 1
                left += 1
        return s[result_start:result_start + min_length] if min_length != float('inf') else ""
