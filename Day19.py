import math
import re
import sys
from collections import deque


def solve(blueprint, t):
    # Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 7 clay. Each geode robot costs 4 ore and 11 obsidian.
    raw_costs = list(map(int, re.findall(r"\d+", blueprint)))
    costs = (
        (raw_costs[1], 0, 0, 0),
        (raw_costs[2], 0, 0, 0),
        (raw_costs[3], raw_costs[4], 0, 0),
        (raw_costs[5], 0, raw_costs[6], 0),
    )

    queue = deque()
    queue.append((t, (0, 0, 0, 0), (1, 0, 0, 0)))
    seen = set()
    best = 0
    max_spend = [max(cost[i] for cost in costs) for i in range(4)]

    while queue:
        t, stuff, robots = queue.popleft()

        min_geodes_left = stuff[3] + (t * robots[3])
        if min_geodes_left > best:
            best = min_geodes_left

        if t == 0 or (t, stuff, robots) in seen:
            continue
        seen.add((t, stuff, robots))

        for resource in range(4):

            # we have enough of this bot?
            if resource != 3 and robots[resource] >= max_spend[resource]:
                continue

            # do we have the bots to get to where we need to be to build this resource next
            if any(
                robots[rid] == 0 for rid, cost in enumerate(costs[resource]) if cost
            ):
                continue

            wait = max(
                [
                    math.ceil((cost - stuff[rid]) / robots[rid])
                    for rid, cost in enumerate(costs[resource])
                    if cost
                ]
                + [0]
            )

            if t - wait - 1 <= 0:
                continue

            next_stuff = [
                stuff[i] + (robots[i] * (wait + 1)) - costs[resource][i]
                for i in range(4)
            ]
            next_robots = list(robots)
            next_robots[resource] += 1

            for i in range(3):
                next_stuff[i] = min(next_stuff[i], max_spend[i] * (t - wait - 1))

            queue.append((t - wait - 1, tuple(next_stuff), tuple(next_robots)))

    return best


with open('Input19.txt', "r") as f:
    lines = f.readlines()

part1 = 0
for i, line in enumerate(lines):
    part1 += (i + 1) * solve(line, 24)
print(f"Part 1: {part1}")

part2 = 1
for line in lines[:3]:
    part2 *= solve(line, 32)
print(f"Part 2: {part2}")











# with open('Input19.txt', 'r') as file:
#     data = file.read()

# fuels = { '=': -2, '-': -1, '0': 0, '1': 1, '2': 2 }
# decimals = dict(map(reversed, fuels.items()))

# numbers = []

# def to_decimal(number):
#     result = sum([(5 ** ii) * fuels[c] for ii, c in enumerate(reversed(number))])
#     return result

# def to_fuel(number):
#     value = []

#     while number > 0:
#         remainder = number % 5
#         if remainder > 2:
#             number += remainder
#             value.append(decimals[remainder - 5])
#         else: 
#             value.append(str(remainder))

#         number //= 5

#     return ''.join(reversed(value))

# for line in data.splitlines():
#     numbers.append(to_decimal(line))

# snafu = to_fuel(sum(numbers))

# print('The SNAFU number to supply to the console is: ' + snafu)