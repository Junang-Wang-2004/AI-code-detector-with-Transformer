class C1:

    def rand10(self):
        while True:
            v1 = rand7()
            v2 = rand7()
            v3 = (v1 - 1) * 7 + v2
            if v3 <= 40:
                return (v3 - 1) % 10 + 1
