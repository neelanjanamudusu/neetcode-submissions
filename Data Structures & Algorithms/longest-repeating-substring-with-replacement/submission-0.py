class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        for i in range(len(s)):
            count = {}
            for j in range(i, len(s)):
                count[s[j]] = count.get(s[j], 0) + 1
                max_freq = max(count.values())
                length = j - i + 1
                if length - max_freq <= k:
                    longest = max(longest, length)
        return longest