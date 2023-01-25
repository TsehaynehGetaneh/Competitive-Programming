class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        print(people)
        
        i = 0
        j = len(people) -1
        while i <= j:
            if i == j:
                count += 1
                break
            elif people[i] + people[j] <= limit:
                count += 1
                i += 1
                j -= 1
            
            else:
                j -= 1
                count += 1
                
        return count if len(people) != 1 else 1
            
        