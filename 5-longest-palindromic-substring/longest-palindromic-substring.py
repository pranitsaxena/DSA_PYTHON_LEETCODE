class Solution:
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s

        start = 0
        max_len = 1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - left - 1

        for i in range(len(s)):
            # Odd length palindrome
            l1, len1 = expand(i, i)

            # Even length palindrome
            l2, len2 = expand(i, i + 1)

            if len1 > max_len:
                start, max_len = l1, len1

            if len2 > max_len:
                start, max_len = l2, len2

        return s[start:start + max_len]