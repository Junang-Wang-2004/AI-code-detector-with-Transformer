class Solution:
    def arrayStringsAreEqual(self, words1, words2):
        def stream(arr):
            for string in arr:
                for ch in string:
                    yield ch
        
        gen1 = stream(words1)
        gen2 = stream(words2)
        
        while True:
            ch1 = next(gen1, None)
            ch2 = next(gen2, None)
            if ch1 != ch2:
                return False
            if ch1 is None:
                return True
