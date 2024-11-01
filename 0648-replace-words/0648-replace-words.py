class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = []

        for root in dictionary:
            roots.append((root, len(root)))
        
        roots.sort(key= lambda item: item[1])
        
        s = sentence.split()

        for i, word in enumerate(s):
            for root in roots:
                if len(root[0]) < len(word) and root[0] == word[:len(root[0])]:
                    s[i] = root[0]
                    break

        return " ".join(s)

        