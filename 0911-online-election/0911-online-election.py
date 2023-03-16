class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leader = []
        d = defaultdict(int)
        max_freq = 0
        for i in range(len(times)):
            d[persons[i]] += 1
            
            if d[persons[i]] >= max_freq:
                self.leader.append((times[i],persons[i]))
                max_freq = d[persons[i]]
        print(self.leader)
    def q(self, t: int) -> int:
         
        
        return self.leader[bisect_left(self.leader,(t,float("inf")))-1][1]

# Your TopVotedCandidate object will be instantiated and called as such: 
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)