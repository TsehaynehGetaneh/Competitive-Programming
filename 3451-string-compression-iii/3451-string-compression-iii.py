class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        left, right = 0, 0

        while left <= right and right < len(word):
            if word[left] == word[right]:
                if (right - left + 1) == 9:
                    comp.append(str(9))
                    comp.append(word[left])
                    right += 1
                    left = right
                else:
                    right += 1

            else:
                comp.append(str(right - left))
                comp.append(word[left])

                left = right
                right += 1

            if right == len(word) and left < len(word):
                comp.append(str(right-left))
                comp.append(word[left])

        return "".join(comp)

        