class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Recursive Function
        # Start at either 0 or 1
        # Can either take 1 step or 2 steps
        # Index are the steps
        # end when reaches past len(cost)

        # Cost of taking a step
        # 0-1: 1
        # 1-2: 2
        # 2-3: 3

        

        def recursive_helper(stepReached, runningCost):
            # if step reaches last step, return running Cost
            if stepReached == len(cost):
                print(f"Reached Final")
                print(f"Step {stepReached} = Final Step:{len(cost)-1}")
                print(f"Current Step: {stepReached}")
                print(f"Running Cost: {runningCost}")
                return runningCost
            # If step reaches past last step, return large number
            if stepReached > len(cost):
                print("Out of Bounds")
                print(f"Current Step: {stepReached}")
                print(f"Running Cost: {runningCost}")
                return len(cost) * 10
            
            print(f"Current Step: {stepReached}")
            print(f"Running Cost: {runningCost}")
            runningCost += cost[stepReached]
            print(f"Cost of Step: {cost[stepReached]}")

            oneStep = recursive_helper(stepReached + 1, runningCost)
            twoStep = recursive_helper(stepReached + 2, runningCost)

            return min(oneStep, twoStep)
            


        return min(recursive_helper(0, 0), recursive_helper(1, 0))