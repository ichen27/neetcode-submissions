class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_diff = 0
        

        for i in range (0, len(prices), 1):
            for j in range (i + 1, len(prices), 1):
                print(i, "|", j)
                if prices[j] - prices[i] > max_diff:
                    max_diff = prices[j] - prices[i]


        return max_diff