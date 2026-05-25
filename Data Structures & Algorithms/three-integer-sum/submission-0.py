class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Given array of numbers
        # Return triplets where the sum of the triplets = 0
        # i, j, k are all distinct
        # No duplicate triplets


        # Brute Force
        # Nested triple for loop and you iterate through every compbination O(n^3)
        
        # Optimize
        ## 1 
        ## Store all values in hash map
        ## Nested for loop to find each combination of twins
        ## Check in hash map to see if their triplet exists
        mem = {}

        for i in nums:
            mem[i] = 1 + mem.get(i, 0)
        

        triplets = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if 0 - (nums[i] + nums[j]) in mem:
                    #print(f"i: {nums[i]}, j: {nums[j]}, 3: {0 - (nums[i] + nums[j])}")
                    temp = sorted([nums[i], nums[j], 0 - (nums[i]+nums[j])])
                    count = dict(Counter(temp))
                    flag = True
                    for k in count:
                        if count[k] > mem[k]:
                            flag = False
                    #print(temp)

                    if temp not in triplets and flag == True:
                        triplets.append(temp)
        
        return triplets





        ## 2
        ## Backtracking solution
        ## Find every combination
        ## append to array if its a triplet that adds up to 0
        