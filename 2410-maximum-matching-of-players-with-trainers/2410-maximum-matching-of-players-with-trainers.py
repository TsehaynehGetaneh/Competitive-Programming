class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players)
        trainers = sorted(trainers)
        
        i = 0
        j = 0
        count = 0
        while i < len(players) and j < len(trainers):
            
            if players[i] <= trainers[j]:
                count += 1
                i += 1
                j += 1
                
            else:
                while j<len(trainers) and trainers[j] < players[i]:
                    j += 1
                 
                if j<len(trainers):
                    count += 1
                    i += 1
                    j += 1
        
        return count
                
                    
        