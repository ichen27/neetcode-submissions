class MinStack:

    def __init__(self):
        # Initialize the attributes of Minstack
        # Create the empty list
        self.stack = []
        self.minIndexes = []
        
    def push(self, val: int) -> None:
        # Push to top of stack
        # Min stack:
        # 5 6 10 2 7 pop pop 
        # Min stack: 5 2
        self.stack.append(val)
        if len(self.minIndexes) == 0:
            self.minIndexes.append(0)
        else:
            if self.stack[len(self.stack) - 1] <= self.stack[self.minIndexes[len(self.minIndexes) - 1]]:
                self.minIndexes.append(len(self.stack) - 1)


    def pop(self) -> None:
        # Pop element at top of stack
        # If its the index at top of min stack, pop min stack as well
        if len(self.stack) <= 0:
            return
        
        if len(self.stack) - 1 == self.minIndexes[len(self.minIndexes) - 1]:
            self.minIndexes.pop()
        
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]
        

    def getMin(self) -> int:
        return self.stack[self.minIndexes[len(self.minIndexes) - 1]]
        
