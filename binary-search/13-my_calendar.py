# You are implementing a program to use as your calendar.
# We can add a new event if adding the event will not cause a double booking.

# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events)

# The event can be represented as a pair of integers start and end that represents a booking on the half-open interval
# [start, end), the range of real numbers x such that start <= x < end.

# Implement the MyCalendar class:
# MyCalendar() Initializes the calendar object.
# boolean book(int start, int end)
# Returns true if the event can be added to the calendar successfully without causing a double booking.
# Otherwise, return false and do not add the event to the calendar.

# Example 1:
# Input ["MyCalendar", "book", "book", "book"] [[], [10, 20], [15, 25], [20, 30]] Output [null, true, false, true]
# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20,
# but not including 20.

# Constraints:
# 0 <= start < end <= 109
# At most 1000 calls will be made to book.

# A potential insertion index idx means that the booking at calendar[idx-1] must come before the new booking,
# and the booking at calendar[idx] must come after the new booking.
# To simplify the searching process, we can deduce that calendar[idx-1] has a start time earlier than start
# and calendar[idx] has a later start time than start.
# Essentially, we are trying to find the leftmost entry such that the start time of this booking is greater
# than start for the new booking.
# We have the feasible function calendar[idx][0] > start, if this condition is true, we will recurse the left half,
# otherwise, recurse the right half.
# To implement the booking behaviour, we will use binary search to find a potential insertion index,
# then check whether the new booking can be actually scheduled into our calendar by checking
# whether the new booking overlaps with calendar[idx-1] and calendar[idx].

# https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        left, right, idx = 0, len(self.calendar) - 1, len(self.calendar)

        while left <= right:
            mid = (left + right) // 2

            if self.calendar[mid][0] > start:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1

        if (idx > 0 and self.calendar[idx - 1][1] > start) or (idx < len(self.calendar) and self.calendar[idx][0] < end):
            return False
        self.calendar.insert(idx, (start, end))

        return True


if __name__ == '__main__':
    new_calendar = MyCalendar()
    print(new_calendar.book(10, 20)) # True
    print(new_calendar.book(15, 25)) # False
    print(new_calendar.book(20, 30)) # True
