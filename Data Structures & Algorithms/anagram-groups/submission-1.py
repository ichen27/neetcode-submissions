class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dict array, array of anagrams, temp array 
        # Iterate through array, convert each string into a dict and append to dict array
        # Then iterate through array with nested for loops and compare every dict
        # If same, then add to temp and then append to anagram array


        # current solution converts each string in array to hashmap and leaves order
        # Convert string to hashmap, append to hash array and append to array of groups of anagram
        # Use hash map array as index key for array of anagram groups
        anagram = []
        dictArr = []
        for index, word in enumerate(strs):
            stringDict = {}
            for l in word:
                if l in stringDict:
                    stringDict[l] += 1
                else:
                    stringDict[l] = 1
            if stringDict not in dictArr:
                dictArr.append(stringDict)
                anagram.append([strs[index]])
            else:
                anagram[dictArr.index(stringDict)].append(strs[index])

        return anagram


        

        """
        i = 0
        j = 0
        while i < len(dictArr):
            temp.clear()
            if i + 1 < len(dictArr):
                j = i + 1
            else:
                temp.append(strs[i])
                if temp not in anagram:
                    anagram.append(temp.copy())
            while j < len(dictArr):
                if dictArr[i] == dictArr[j]:
                    if strs[i] not in temp:
                        temp.append(strs[i])
                    if strs[j] not in temp:
                        temp.append(strs[j])
                    strs.pop(j)
                    dictArr.pop(j)
                    j-=1
                j += 1

            i += 1
            j = 0
            if temp not in anagram:
                anagram.append(temp.copy())


            
        return anagram

        """

