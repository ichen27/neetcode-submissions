class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra Algorithm
        # DFS algorithm using min heap
        # Visit first node, update min heap, nodes on min heap ordered by travel time
        # visit the node at the top of the heap and pop that it off the heap
        # Update the hash with the nodes its connected to and add those nodes to the heap
        # Keep running until there is nothing left on the heap
        # Hash starts default with values of -1 so return -1 if there is still -1 on the list
        
        # Start at node 2
        # 2 connects to 1; weight 1
        # 2 connects to 3; weight 1
        # 3 connects to 4; weight 1



        # Start node 2, 2 nodes total
        # 1 connects to 2; weight 1
        # 2 connects to 1; weight 3

        node_heap = []
        min_hash = {}
        #visited_hash = {}

        # Makes all values in the hash = -1
        for i in range(1, n+1):
            min_hash[i] = -1
            #vistied_hash[i] = False

        # Sets the value of node k to 0
        min_hash[k] = 0
    
        # node_heap: [time to reach node, source, target, unvisited since last update]
        heapq.heappush(node_heap, [0, k, k])

        # Runs as long as there are values in the heap
        while len(node_heap) > 0:
            # Choose a node that hasn't been visited since last update
            minNode = node_heap[0]
            """
            while True:
                if visited_hash[minNode[2]] == True:
                    heapq.heappop(node_heap)
                    heapq.heapify(node_heap)
                    minNode = node_heap[0]
                else:
                    break
            
            visited_hash[minNode[2]] = True
            """
            # Iterates through every node in times
            for node in times:
                # Check if visited since weight got updated
                # if the node at the top of the node heap is equal to any source node in times
                # For the node at the top of the heap, find all nodes it is connected to 
                if minNode[2] == node[0]:
                    # Updating the hash
                    # Checks if the time value stored at that node in the hash is greater than the new time
                    # Or if the value stored at that node is -1 (never updated)
                    newTime = min_hash[node[0]] + node[2]
                    if min_hash[node[1]] > newTime or min_hash[node[1]] == -1:
                        # Update the value of the target node with the new weight
                        min_hash[node[1]] = newTime
                        heapq.heappush(node_heap, [newTime, node[0], node[1]])
                        #visted_hash[node[1]] = False
                        
            # Pop the value at the top of the heap
            heapq.heappop(node_heap)
            # Create min heap
            heapq.heapify(node_heap)

        if -1 in min_hash.values():
            return -1


        high = 0
        for key, value in min_hash.items():
            if value > high:
                high = value


        return high


                    







