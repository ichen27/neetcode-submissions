class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        x = 0
        y = 0
        for i in range(len(stones)):
            stones[i] = stones[i] * -1

        while len(stones) > 1:
            heapq.heapify(stones)
            x = -heapq.heappop(stones)
            heapq.heapify(stones)
            y = -heapq.heappop(stones)

            if x < y:
                y = y - x
                heapq.heappush(stones, -y)
            elif y < x:
                x = x - y
                heapq.heappush(stones, -x)

        if len(stones) > 0:
            return -stones[0]
        else:
            return 0





