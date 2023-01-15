class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        dic = Counter(words[0])
        
        for i in range(1,len(words)):
            word = Counter(words[i])
            
            for key in word:
                if key in dic and dic[key] > word[key]:
                    dic[key] = word[key]
                    
            for key,val in list(dic.items()):
                if key not in word:
                    del dic[key]        
            
        output = []          
        for key,val in dic.items():
            char = list(key*val)
            output.extend(char)
            
            
        return output
                    
        