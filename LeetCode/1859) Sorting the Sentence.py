class Solution:
    def sortSentence(self, s: str) -> str:
        sortedWord = [0] * len(s.split())
        sortedSentence = " "
        for word in s.split():
            index = int(word[-1])
            newWord = word[:-1]
            sortedWord[index-1] = newWord
        
        return sortedSentence.join(sortedWord)