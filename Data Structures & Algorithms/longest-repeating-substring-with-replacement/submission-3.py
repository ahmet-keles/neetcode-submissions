class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        maxLen = 0
        maxFreq = 0
        for i in range(len(s)):
            count[s[i]] += 1
            maxFreq = max(maxFreq, count[s[i]])
            if (i - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            maxLen = max(maxLen, i - left + 1)
        return maxLen

