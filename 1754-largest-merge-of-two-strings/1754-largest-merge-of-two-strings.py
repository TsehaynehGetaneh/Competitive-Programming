class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        output = []
        i = 0
        j = 0
        
        while i<len(word1) and j<len(word2):
            if word1[i] > word2[j]:
                output.append(word1[i])
                i += 1
            
            elif word2[j] > word1[i]:
                output.append(word2[j])
                j += 1
            
            else:
                if word1[i+1:] > word2[j+1:]:
                    output.append(word1[i])
                    i += 1
                elif word2[j+1:] > word1[i+1:]:
                    output.append(word2[j])
                    j += 1
                else:
                    output.append(word1[i])
                    i += 1
            
        
        while i < len(word1):
            output.append(word1[i])
            i += 1
            
        while j < len(word2):
            output.append(word2[j])
            j += 1
            
            
        return "".join(output)
            
        