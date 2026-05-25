class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Using recursion backtracking approach
        # Recursively traverse the string
        # For each traversal, store whether that portion of the string is in word dict
        # For each traversal, decide wether to break or keep moving
        ## If break then cut off all all prev
        # Base case returns true, if any path returns true, then return true
        
        mem = {}

        def dp_words(left, right):

            # Base Case: if left pointer == len(s)
            if left == len(s):
                return True
            if right == len(s):
                return False

            # Call 2: Check if word is in
            ## Check if in dict
            ## If not in dict then 
            ## If yes, then recursive call and move left and right pointer past word
            # If any call returns True, return True automatically
            found = False
            if s[left:right+1] in wordDict:
                if (left, right) in mem:
                    return mem[(left, right)]
                
                found = dp_words(right + 1, right + 1)

                
            # Call 1: Move right pointer
            skip = dp_words(left, right + 1)

            mem[(left, right)] = skip or found

            if skip or found:
                return True
            else:
                return False


        return dp_words(0, 0)





        