class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashedLetters = defaultdict(int)
        for letter in s:
            hashedLetters[letter] += 1

        for letter2 in t:
            hashedLetters[letter2] -= 1
        
        return all(value == 0 for value in hashedLetters.values())