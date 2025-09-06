# An employee is given a list of N tasks. A deadline is associated with each task and some reward points are allotted to the employee if the corresponding tasks are completed within the deadline. Every task takes one unit of time to get completed and only one task can be done at a time. The minimum possible deadline for any task is 1. Write a program to determine the order of task execution to maximize the total rewards points for the employee.

# Input: {task_id, deadline, reward_points} list: {{ 'a', 2, 80 }, { 'b', 1, 19 }, { 'c', 2, 27 }, { 'd', 3, 15 }}

# Output:
# Tasks completion order: a c d
# Maximum reward points: 122

# test case 2
# {{ 'a', 2, 80 }, { 'b', 1, 19 }, { 'c', 1, 27 }, { 'd', 1, 15 }}
# Tasks completion order: c a
# Maximum reward points: 107

# case 3
# [[ 'a', 2, 80 ], [ 'b', 1, 27 ], [ 'c', 1, 27 ]]

# case 4
# [[ 'a', 1, 40 ], [ 'b', 2, 10 ], [ 'c', 3, 30 ], [ 'd', 3, 20 ]]

def max_reward(tasks):
    if not tasks:
        return [], 0
    max_duration = max([task[1] for task in tasks])
    perm_list = permutation(tasks)
    max_points = 0
    max_points_order = []
    cache = dict()
    for perm in perm_list:
        time_lapse = 0
        points = 0
        points_order = []
        k = ""
        for t in perm:
            time_lapse += 1
            if time_lapse > t[1] or time_lapse > max_duration:
                break
            k += t[0]
            if k in cache:
                points = cache[k]
            else:
                points += t[2]
                cache[k] = points
            points_order.append(t[0])

        if points > max_points:
            max_points = points
            max_points_order = points_order[:]
    print(max_points_order, max_points)
    return max_points_order, max_points


def permutation(tasks):
    results = []
    helper([], tasks, results)
    return results


def helper(prev, cur, results):
    if len(cur) == 0:
        results.append(prev)
    for i, item in enumerate(cur):
        helper(prev + [item], cur[:i] + cur[i + 1:], results)


# max_reward([['a', 2, 80], ['b', 1, 19], ['c', 2, 27], ['d', 3, 15]])
max_reward([['a', 2, 80], ['b', 1, 19], ['c', 1, 27], ['d', 1, 15]])
max_reward([['a', 2, 80], ['b', 1, 27], ['c', 1, 27]])
max_reward([['a', 1, 40], ['b', 2, 10], ['c', 3, 30], ['d', 3, 20]])
