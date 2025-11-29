import re

class Solution:
    def diffWaysToCompute(self, s):
        parts = re.findall(r'\d+|[+\-*]', s)
        values = []
        opers = []
        for part in parts:
            if part in '+-*':
                opers.append(part)
            else:
                values.append(int(part))
        num_count = len(values)
        table = [[[] for _ in range(num_count)] for _ in range(num_count)]
        for idx in range(num_count):
            table[idx][idx] = [values[idx]]
        for span in range(2, num_count + 1):
            for begin in range(num_count - span + 1):
                finish = begin + span - 1
                for cut in range(begin, finish):
                    lres = table[begin][cut]
                    rres = table[cut + 1][finish]
                    oper = opers[cut]
                    for lv in lres:
                        for rv in rres:
                            if oper == '+':
                                table[begin][finish].append(lv + rv)
                            elif oper == '-':
                                table[begin][finish].append(lv - rv)
                            else:
                                table[begin][finish].append(lv * rv)
        return table[0][num_count - 1]
