class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1

        left = 0
        right = 0
        subStringSize = 0
        mem = set()

        while right < len(s):
            
            if s[right] not in mem:
                mem.add(s[right])
                subStringSize = max(subStringSize, right - left + 1)
                right += 1

            else:
                mem.remove(s[left])
                left += 1

        return subStringSize