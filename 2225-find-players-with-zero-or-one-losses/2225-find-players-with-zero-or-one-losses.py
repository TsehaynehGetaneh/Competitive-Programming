class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = {}
        winner = set()
        looser = []
        
        for match in matches:
            if match[1] in d:
                d[match[1]] += 1
            else:
                d[match[1]] = 1
        
        for match in matches:
            if match[0] not in d:
                winner.add(match[0])
        
        for key, val in d.items():
            if val == 1:
                looser.append(key)
        
        winner = list(winner)
        winner.sort()
        looser.sort()
        
        return [winner, looser]
                
        
        