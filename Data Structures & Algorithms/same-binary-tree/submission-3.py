# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS approach
        # Using queue and dequeue

        d = deque()

        d.append((p, q))

        # Iterate to each node, compare, if equal append children to queue, if not, return
        while len(d) > 0:
            if d[0][0] == None and d[0][1] == None:
                d.popleft()
            elif d[0][0] == None or d[0][1] == None:
                return False
            else:
                if d[0][0].val == d[0][1].val:
                    d.append((d[0][0].left, d[0][1].left))
                    d.append((d[0][0].right, d[0][1].right))
                    d.popleft()
                else:
                    return False

        return True





        