class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Max Proft
        # Buy and sell multiple times
        # Can treat it as a backtracking problem, looking at every combination
        # Memoization:
        ## Store the max value through recursion call with the following actions:
        ### Buy and move on, sell and move on(cannot buy following day), or just move on

        mem = {}
        # dynamic programming, recursive function
        # Arguments: Index, owned(yes or no) own stock
        # owned: 1 own stock, 0 no stock
        def dp_stock(index, owned):
            # Base case
            # When reaches out of index of prices
            # return 0
            if index >= len(prices):
                return 0

            # Each recursive call adds or subtracts from total
            # Buy coin : subtract value
            # Sell coin: add value
            # No action: None
            # Set conditions and store different variations in the hashmap
            if (index, owned) in mem:
                return mem[(index, owned)]
            else:
                if owned == 1: # Own the stock
                    mem[(index, owned)] = max(dp_stock(index + 2, 0) + prices[index], dp_stock(index + 1, 1))
                elif owned == 0: # Don't own stock
                    mem[(index, owned)] = max(dp_stock(index + 1, 1) - prices[index], dp_stock(index + 1, 0))
                
            return mem[(index, owned)]

        
        return dp_stock(0, 0)