class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy algorithm
        # Kind of like stairs problem
        # Think about problem in reverse
        # Think about all the indexes that can reach the last index

        # Iterate backwards
        # Goal starts at last index
        # Goal is required index that must be hit to reach the end
        # If you find smaller index that can hit current goal, that that become new goal
        # True onces index 0 becomes goal
        if len(nums) == 0:
            return False

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

            if goal == 0:
                return True

        return False

            
