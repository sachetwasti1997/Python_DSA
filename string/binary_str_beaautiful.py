class Solution:
    def minChanges(self, s: str) -> int:
        l, r, res = 0, 1, 0
        while r < len(s):
            if s[l] != s[r]:
                res += 1
            l += 2
            r += 2
        return res
    
s = Solution()

res = s.minChanges("1001")
print(res)