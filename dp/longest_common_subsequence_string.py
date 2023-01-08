
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = len(text1)
        col = len(text2)
        dp=[[0 for i in range(col+1)] for j in range(row+1)]
        ans = 0
        for i in range(1,row+1):
            for j in range(1,col+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
                ans = max(ans,dp[i][j])
        
        return ans

sol = Solution()
a = "abcba"
b = "abcbcba"
print(sol.longestCommonSubsequence(a,b))