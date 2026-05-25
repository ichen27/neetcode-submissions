class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hash map
        # Iterate through array
        # If number is not in hash map, add to hash map and = 1
        # If alr in hash map += 1 to the current value
        # Loop k times and append k integers to array


        num_hash = {}

        for i in nums:
            if i in num_hash:
                num_hash[i] += 1
            else:
                num_hash[i] = 1
        

        topK = sorted(num_hash.items(), key=lambda x: x[1], reverse=True)[:k]
        
        topList = []
        for i in topK:
            topList.append(i[0])

        return topList



        