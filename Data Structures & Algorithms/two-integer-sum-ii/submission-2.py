class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointers
        # Brute force solution:
        ## Nested for loop, iterates through every combination
        # Optimization 1:
        ## Once sum is over target, inner loop cannot iterate past the index that surpassed the sum
        # Optimization 2:
        ## Nested loops iterating towards eachother
        ## Once reaches under target, move on
        ## Starts from previous ceiling
        ## Each time the sum > target, make that index the new ceiling and start inner loop from that 


        ceiling = len(numbers)
        

        for i in range(0, ceiling):
            for j in range(ceiling - 1, i, -1):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
                elif numbers[i] + numbers[j] > target:
                    ceiling -= 1
                elif numbers[i] + numbers[j] < target:
                    break