class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        n = len(req_skills)
        target = (1 << n) - 1
        skill_index = {skill: idx for idx, skill in enumerate(req_skills)}
        masks = []
        for skills in people:
            mask = 0
            for skill in skills:
                if skill in skill_index:
                    mask |= 1 << skill_index[skill]
            masks.append(mask)
        INF = float('inf')
        min_team_size = [INF] * (1 << n)
        min_team_size[0] = 0
        predecessor = [None] * (1 << n)
        for i in range(len(people)):
            pmask = masks[i]
            for state in range(1 << n):
                if min_team_size[state] == INF:
                    continue
                next_state = state | pmask
                if next_state == state:
                    continue
                candidate_size = min_team_size[state] + 1
                if candidate_size < min_team_size[next_state]:
                    min_team_size[next_state] = candidate_size
                    predecessor[next_state] = (state, i)
        result = []
        state = target
        while state != 0:
            prev_state, person_id = predecessor[state]
            result.append(person_id)
            state = prev_state
        result.reverse()
        return result
