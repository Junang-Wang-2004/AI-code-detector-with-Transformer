class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        hours = 0
        current_energy = initialEnergy
        current_experience = initialExperience
        n = len(energy)
        for i in range(n):
            enemy_energy = energy[i]
            enemy_experience = experience[i]
            if current_energy <= enemy_energy:
                shortage = enemy_energy + 1 - current_energy
                hours += shortage
                current_energy += shortage
            current_energy -= enemy_energy
            if current_experience <= enemy_experience:
                shortage = enemy_experience + 1 - current_experience
                hours += shortage
                current_experience += shortage
            current_experience += enemy_experience
        return hours
