class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Coins = list of coin options
        # amount = target amount of money
        # Brute Force: 
        ## Using recursion, iterate through every possible combination
        
        # Kind of like subset problem with backtracking
        # where each call either doesn't add anything or does and then moves on
        # either add current or move to next
        # If the add goes > amount, then recusively call the smaller coins
        ## Stops once it reaches amount
        ## Or if amount is greater and the current coin the is the smallest


        # Optimizers:
        ## Store value and counts
        
        # max of amount of dollars amount is + 10
        prevCoins = {}

        def coin_combinator(i, value, count):
            # Base cases:
            # If index exceeds the final index
            # If value exceeds amount
            # print(f"i: {i}, value: {value}, count: {count}")
            if (i, value, count) in prevCoins:
                return prevCoins[(i, value, count)]
            
            if i >= len(coins) or value > amount:
                return amount + 10
        
            # Update minCount whenever value = amount
            # Check which is smaller
            if value == amount:
                return count

            # For each recursive call
            ## Move to next coin without updating
            ## Or 
            ## Add current coin, stay at current coin, update value and count
            newValue = value + coins[i]
            newCount = count + 1


            prevCoins[(i, value, count)] = min(coin_combinator(i+1, value, count), coin_combinator(i, newValue, newCount))
            
            return prevCoins[(i, value, count)]

        minCount = coin_combinator(0, 0, 0)

        if minCount > amount:
            return -1
        else:
            return minCount




