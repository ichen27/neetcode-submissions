class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Recursive function
        # has index of both words
        
        mem = {}

        def recursiveTraversal(index1, index2):
            # Traverses until an index reaches end of its string
            if index1 >= len(text1) or index2 >= len(text2):
                return 0

            if (index1, index2) in mem:
                return mem[(index1, index2)]

            # Conditional for if the letter at index1 is equal to index 2
            if text1[index1] == text2[index2]:
                # Recursive all explores all combinations
                ## All combinations of every index1
                ## All combinations of every index2
                mem[(index1, index2)] = 1 + recursiveTraversal(index1 + 1, index2 + 1)
                return mem[(index1, index2)]
            else:
                mem[(index1, index2)] = max(recursiveTraversal(index1 + 1, index2), recursiveTraversal(index1, index2 + 1))
                return mem[(index1, index2)] 


        return recursiveTraversal(0, 0)