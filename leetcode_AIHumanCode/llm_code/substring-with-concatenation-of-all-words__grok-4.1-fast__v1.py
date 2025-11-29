from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        word_length = len(words[0])
        num_words = len(words)
        total_length = num_words * word_length
        if len(s) < total_length:
            return []
        freq_map = Counter(words)
        result_list = []
        for offset in range(word_length):
            window_count = Counter()
            window_size = 0
            window_start = offset
            for curr_end in range(offset, len(s) - word_length + 1, word_length):
                current_word = s[curr_end:curr_end + word_length]
                if current_word not in freq_map:
                    window_count.clear()
                    window_size = 0
                    window_start = curr_end + word_length
                    continue
                window_count[current_word] += 1
                window_size += 1
                while window_count[current_word] > freq_map[current_word]:
                    left_word = s[window_start:window_start + word_length]
                    window_count[left_word] -= 1
                    window_size -= 1
                    window_start += word_length
                if window_size == num_words:
                    result_list.append(window_start)
        return result_list
