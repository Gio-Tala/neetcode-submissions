class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_len = 0
        curr_len = 0
        for i in range(len(s)):
            curr_len += 1
            if s[i] in seen:
                while s[left] != s[i]:
                    curr_len -= 1
                    seen.discard(s[left])
                    left += 1

                left += 1
            seen.add(s[i])
            max_len = max(i-left+1, max_len)
        
        return max_len
