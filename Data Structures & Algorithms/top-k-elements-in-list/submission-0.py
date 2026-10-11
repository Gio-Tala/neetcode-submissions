class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashed_frequencies = defaultdict(int)

        for num in nums:
            hashed_frequencies[num] += 1
        

        sorted_freqs = sorted([(value, key) for key, value in hashed_frequencies.items()])

        outp = []
        len_sorted_freqs = len(sorted_freqs)
        for i in range(k):
            #print(sorted_freqs.pop()[0])
            outp.append(sorted_freqs.pop()[1])
        
        return outp