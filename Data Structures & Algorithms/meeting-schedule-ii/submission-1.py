"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Find minimum number of days to schedule all meetings without conficts

        # Min heap by start time
        # Iterate through by taking interval objects that fit the criteria
        # Put unused itervals in new ones
        # Take interval object
        # Repeat using new array of interval objects
        unusedTimes = []
        for i in intervals:
            unusedTimes.append((i.start, i.end))
        usedTimes = []
        days = 0

        unusedTimes.sort()


        while len(unusedTimes) > 0:
            intervals = unusedTimes
            print(f"Intervals: {intervals}")
            unusedTimes = []
            days += 1
            for i in intervals:

                if len(usedTimes) == 0:
                    #print("1")
                    usedTimes.append(i)
                elif usedTimes[-1][1] <= i[0]:
                    #print("2")
                    usedTimes.append(i)
                else:
                    #print("3")
                    unusedTimes.append(i)
            print(f"used: {usedTimes}")
            print(f"unused: {unusedTimes}")
            usedTimes = []

        return days








