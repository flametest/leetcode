# Given an array of meeting time intervals consisting of
# start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
# Example 1:
#
# Input: [[0,30],[5,10],[15,20]]
# Output: false
#
# Example 2:
# Input: [[7,10],[2,4]]
# Output: true


def test1(input_list):
    if len(input_list) == 0:
        return True
    sorted_list = sorted(input_list, key=lambda x: x[0])
    prev_end = cur_start = 0
    for idx, (start, end) in enumerate(sorted_list):
        if idx == 0:
            prev_end = end
            continue
        cur_start = start
        if cur_start <= prev_end:
            return False
        prev_end = end
    return True


# Given an array of meeting time intervals consisting of
# start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
# Example 1:
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
#
# Example 2:
# Input: [[7,10],[2,4]]
# Output: 1

def test2(input_list):
    if len(input_list) == 0:
        return 0
    max_len = max([t[1] for t in input_list])
    results = [0] * (max_len + 1)
    for start, end in input_list:
        results[start] = 1
        results[end] = -1
    max_room = 0
    tmp = 0
    for i in results:
        tmp = tmp + i
        max_room = max(tmp, max_room)
    return max_room


# You are given an integer n. There are n rooms numbered from 0 to n - 1.
#
# You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that
# a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.
#
# Meetings are allocated to rooms in the following manner:
#
# Each meeting will take place in the unused room with the lowest number.
# If there are no available rooms, the meeting will be delayed until a room becomes free. The del
# The delayed meeting should have the same duration as the original meeting.
# When a room becomes unused, meetings that have an earlier original start time should be given the room.
# Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.
#
# A half-closed interval [a, b) is the interval between a and b including a and not including b.

# Example 1:
#
# Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
# Output: 0
# Explanation:
# - At time 0, both rooms are not being used. The first meeting starts in room 0.
# - At time 1, only room 1 is not being used. The second meeting starts in room 1.
# - At time 2, both rooms are being used. The third meeting is delayed.
# - At time 3, both rooms are being used. The fourth meeting is delayed.
# - At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
# - At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
# Both rooms 0 and 1 held 2 meetings, so we return 0.

next_room_available = 1  # room_index

room_dict = {
    0: [[0, 10], [10, 11]],
    1: [[1, 5], [5, 10]]
}
# n*m

# for meeting in meetings:


if __name__ == '__main__':
    print(test2([[0, 30], [5, 10], [15, 20]]))
    print(test2([[7, 10], [2, 4]]))
