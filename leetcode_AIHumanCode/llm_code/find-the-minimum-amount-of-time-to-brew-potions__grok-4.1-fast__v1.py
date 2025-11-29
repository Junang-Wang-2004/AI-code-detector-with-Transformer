class Solution:
    def minTime(self, skills, manas):
        prefixes = [0]
        for val in skills:
            prefixes.append(prefixes[-1] + val)
        ans = manas[-1] * prefixes[-1]
        for i in range(1, len(manas)):
            prev_mana = manas[i - 1]
            next_mana = manas[i]
            max_val = 0
            for j in range(len(skills)):
                pref = prefixes[j + 1]
                last_skill = skills[j]
                contrib = (prev_mana - next_mana) * pref + next_mana * last_skill
                if contrib > max_val:
                    max_val = contrib
            ans += max_val
        return ans
