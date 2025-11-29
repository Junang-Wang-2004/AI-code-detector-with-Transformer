class Solution(object):
    def read(self, buf, n):
        count = 0
        temp = [''] * 4
        while count < n:
            fetched = read4(temp)
            if fetched == 0:
                break
            num_to_copy = min(fetched, n - count)
            buf[count:count + num_to_copy] = temp[:num_to_copy]
            count += num_to_copy
        return count
