class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # array of nums and target integer
        # Return a list of all unique combinations of nums taht sum to target
        # same number can be used unlimited times


        # Backtracking
        # Choose current or skip
        # Base case whenever reaches end of nums or sum > target

        # Return array of arrays
        ret = []
        mem = {}

        # Take index, combination array, and running total
        def dfs(index, combination, running):
            # Base Cases
            # If running grows larger than target
            # Index exceeds array length
            if running > target:
                return
            elif index >= len(nums):
                return
            if tuple(combination) in mem:
                return

            # Main return
            # If running sum equals to target
            # Append to return array
            # and return
            if running == target:
                print(f"Running: {running}, Array: {combination}")
                ret.append(combination)
                return
            

            # Recursive backtracking calls
            # 1: Move to next index
            dfs(index + 1, combination.copy(), running)
            
            # 2: Add to combination
            combination.append(nums[index])
            running += nums[index]
            dfs(index, combination.copy(), running)

            mem[tuple(combination)] = 1

            return


        dfs(0, [], 0)
        return ret
        