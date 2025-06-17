MOD = 10**9 + 7

class Solution:
    def countGoodArrays(self, n, m, k):
        prev = [0] * (k + 1)
        prev[0] = m  # Base case: for length 1, 0 adjacent matches

        for i in range(2, n + 1):
            curr = [0] * (k + 1)
            for j in range(0, min(i, k + 1)):
                # Case 1: choose different → no new match
                curr[j] = prev[j] * (m - 1) % MOD
                # Case 2: repeat → adds one match
                if j > 0:
                    curr[j] = (curr[j] + prev[j - 1]) % MOD
            prev = curr  # update for next iteration

        return prev[k]
