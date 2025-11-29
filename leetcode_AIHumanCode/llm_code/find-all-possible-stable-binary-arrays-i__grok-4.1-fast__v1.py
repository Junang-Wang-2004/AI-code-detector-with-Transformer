class Solution:
    def numberOfStableArrays(self, num_zeros, num_ones, max_run):
        MOD = 10**9 + 7
        end0 = [[0] * (num_ones + 1) for _ in range(num_zeros + 1)]
        end1 = [[0] * (num_ones + 1) for _ in range(num_zeros + 1)]
        for z in range(num_zeros + 1):
            end0[z][0] = 1 if z <= max_run else 0
        for o in range(num_ones + 1):
            end1[0][o] = 1 if o <= max_run else 0
        for z in range(1, num_zeros + 1):
            for o in range(1, num_ones + 1):
                end0[z][o] = (end0[z - 1][o] + end1[z - 1][o]) % MOD
                if z > max_run:
                    end0[z][o] = (end0[z][o] - end1[z - max_run - 1][o]) % MOD
                end1[z][o] = (end0[z][o - 1] + end1[z][o - 1]) % MOD
                if o > max_run:
                    end1[z][o] = (end1[z][o] - end0[z][o - max_run - 1]) % MOD
        return (end0[num_zeros][num_ones] + end1[num_zeros][num_ones]) % MOD
