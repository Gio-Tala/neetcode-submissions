class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashed_hashes = defaultdict(list)
        for i, word in enumerate(strs):
            hashed_list = [0] * 26
            for letter in word:
                hashed_list[ord(letter) - 97] += 1
            
            hashed_hashes[tuple(hashed_list)].append(word)
        
        outp = []

        for val in hashed_hashes.values():
            outp.append(val)
        
        return outp


