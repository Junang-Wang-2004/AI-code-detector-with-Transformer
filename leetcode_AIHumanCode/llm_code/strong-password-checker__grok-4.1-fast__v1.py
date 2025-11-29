class Solution:
    def strongPasswordChecker(self, password):
        n = len(password)
        has_low = any(c.islower() for c in password)
        has_up = any(c.isupper() for c in password)
        has_dig = any(c.isdigit() for c in password)
        missing = 3 - int(has_low) - int(has_up) - int(has_dig)
        repl = 0
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        i = 0
        while i < n:
            start = i
            while i < n and password[i] == password[start]:
                i += 1
            ln = i - start
            if ln >= 3:
                repl += ln // 3
                rem = ln % 3
                if rem == 0:
                    cnt1 += 1
                elif rem == 1:
                    cnt2 += 1
                else:
                    cnt3 += 1
        if n < 6:
            return max(missing, 6 - n)
        if n <= 20:
            return max(missing, repl)
        to_del = n - 20
        save = 0
        rem_del = to_del
        save1 = min(rem_del, cnt1)
        save += save1
        rem_del -= save1
        save2 = min(rem_del // 2, cnt2)
        save += save2
        rem_del -= save2 * 2
        save3 = min(rem_del // 3, cnt3)
        save += save3
        return to_del + max(missing, repl - save)
