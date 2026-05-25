class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # Two pointers
        


        pointer1 = 0
        pointer2 = 0
        new_word = ""

        while pointer1 < len(word1) and pointer1 < len(word2):
            new_word += word1[pointer1]
            new_word += word2[pointer1]


            pointer1 += 1

        if len(word1) > len(word2):
            new_word += word1[pointer1:]
        elif len(word2) > len(word1):
            new_word += word2[pointer1:]
        
        return new_word

        