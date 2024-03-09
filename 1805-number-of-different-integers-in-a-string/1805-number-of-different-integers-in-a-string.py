class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        data = set()
        left, right = 0, 0

        while left <= right and right < len(word):
            if word[right].isdigit():
                while right < len(word) and word[right].isdigit():
                    right += 1

                data.add(int(word[left:right]))
                left = right

            else:
                left += 1
                right += 1
        print(data)
        return len(data)
        