class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        skills = []
        total_chemistry = 0
        
        skill_sum = skill[0] + skill[-1]
        
        i = 0
        j = len(skill) -1
        while i < j:
            if skill[i] + skill[j] != skill_sum:
                return -1
            
            skills.append((skill[i],skill[j]))
            i += 1
            j -= 1
            
        for i in range(len(skills)):
            total_chemistry += (skills[i][0]*skills[i][1])
            
        
        return total_chemistry
            
        