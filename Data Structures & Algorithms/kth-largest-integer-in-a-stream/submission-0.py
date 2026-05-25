class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Always returns the kth largests num for each add
        self.k = k
        self.nums = nums
        for i in range(len(self.nums)):
            self.nums[i] = self.nums[i] * -1
        heapq.heapify(self.nums)
        print(self.nums)


    def findKthLargest(self) -> int:
        temp = self.nums.copy()
        tempArr = []
        for i in range(self.k):
            tempArr.append(-heapq.heappop(temp))
            heapq.heapify(temp)
        
        print(f"Largest to Smallest: {tempArr}")
        return tempArr[len(tempArr) - 1]
        

    def add(self, val: int) -> int:
        print(f"Pushing {val}")
        print(f"Before {self.nums}")
        heapq.heappush(self.nums, -val)
        print(f"After {self.nums}")
        heapq.heapify(self.nums)
        kLargest = self.findKthLargest()
        print(f"Heap: {self.nums}, {self.k}th largest: {kLargest}")
        return kLargest
        
        
