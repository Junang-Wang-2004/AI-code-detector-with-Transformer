class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        def char_freq(text):
            counts = [0] * 26
            for ch in text:
                if ch.isalpha():
                    counts[ord(ch.lower()) - ord('a')] += 1
            return counts

        plate_counts = char_freq(licensePlate)

        def is_completing(w):
            word_counts = char_freq(w)
            return all(word_counts[i] >= plate_counts[i] for i in range(26))

        matching_words = [w for w in words if is_completing(w)]
        return min(matching_words, key=len) if matching_words else None
