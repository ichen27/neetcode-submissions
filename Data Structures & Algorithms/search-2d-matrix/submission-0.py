class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search of first column and every row, vertical
        # first integer > last integer of previous row
        # Want either find:
        ## Best case: find target
        ## Find the 2 rows where the first integer is less than and greater than the target

        # Use binary search on first element of each row
        # Reach final number, where start and end are the same
        # If less than, iterate until reaches row with greater and the prev row is the row to explore
        # If greater than, iterate until column with smaller integer

        # Then binary search the row with smaller integer


        # 1 2 3 4 5 -> len = 5, mid = 2
        # 1 2 3 4 -> len = 4, mid = 2
        # If number is greater, end = mid - 1, start stays the same, recalculate mid
        # If number is less, start = mid + 1, end stays the same, recalculate mid

        start = 0
        end = len(matrix) - 1
        mid = int((start + end) / 2)
        while matrix[mid][0] != target and start != end:

            if matrix[mid][0] > target:
                if start != mid:
                    end = mid - 1
                else:
                    end -= 1
            elif matrix[mid][0] < target:
                start = mid + 1
            mid = int((start + end) / 2)
    
        if matrix[mid][0] == target:
            return True


        if matrix[mid][0] > target:
            mid -= 1



        row = mid
        start = 0
        end = len(matrix[row]) - 1
        mid = int((start + end) / 2)


        while matrix[row][mid] != target and start != end:
            print(f"start: {start}, end: {end}, mid: {mid}")
            if matrix[row][mid] > target:
                if start != mid:
                    end = mid - 1
                else:
                    end -= 1
            elif matrix[row][mid] < target:
                start = mid + 1

            mid = int((start + end) / 2)


        if matrix[row][mid] == target:
            return True
        else:
            return False
            
        







        