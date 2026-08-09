

class Solution:
    def getMin(self , dp , target , squares):
        idx = 0
        min_num = target + 1
        min_select = 0
        while idx < len(squares):
            cur_square = squares[idx]
            if target - cur_square < 0:
                break
            tar = dp[target - cur_square] + 1
            if tar < min_num:
                min_num = tar
                min_select = cur_square
            idx += 1
        return min_num , min_select

    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(1,n+1):
            if i * i <= n+1:
                squares.append(i * i)
            else:
                break
        dp = [n + 1 for _ in range(n+1)]
        select = [0 for _ in range(n+1)]

        dp[0] , select[0] = 0 , 0
        for i in range(1 , n+1):
            min_pre , min_select = self.getMin(dp , i , squares)
            dp[i] = min_pre
            select[i] = min_select

        return dp[n]

if __name__ == "__main__":
    solution = Solution()
    test_data = 12
    print(solution.numSquares(test_data))