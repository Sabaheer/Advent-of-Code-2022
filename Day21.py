import sys


def get_val(m):
    ex = monkeys[m]
    try:
        return int(ex)
    except ValueError:
        pass

    toks = ex.split(' ')
    assert len(toks) == 3

    match toks[1]:
        case '+':
            return get_val(toks[0]) + get_val(toks[2])
        case '-':
            return get_val(toks[0]) - get_val(toks[2])
        case '*':
            return get_val(toks[0]) * get_val(toks[2])
        case '/':
            return get_val(toks[0]) / get_val(toks[2])
    assert False

def get_val2(m, humn):
    if m == 'humn':
        return humn
    ex = monkeys[m]
    try:
        return int(ex)
    except ValueError:
        pass

    toks = ex.split(' ')
    assert len(toks) == 3


    if m == 'root':
        v1 = get_val2(toks[0], humn)
        v2 = get_val2(toks[2], humn)
        return (v1 == v2, v1, v2)

    if toks[1] == '+':
        return get_val2(toks[0], humn) + get_val2(toks[2], humn)
    if toks[1] == '-':
        return get_val2(toks[0], humn) - get_val2(toks[2], humn)
    if toks[1] == '*':
        return get_val2(toks[0], humn) * get_val2(toks[2], humn)
    if toks[1] == '/':
        return get_val2(toks[0], humn) / get_val2(toks[2], humn)
    assert False


with open("Input21.txt", 'r') as f:
    lines = f.readlines()

monkeys = {}
for line in lines:
    # scms: zhsc + plrj
    m, ex = line.strip().split(': ')
    monkeys[m] = ex

part1 = int(get_val('root'))
print(f'Part 1: {part1}')

lo = -1e20
hi = 1e20
mid = 0
while True:
    eq, v1, v2 = get_val2('root', mid)
    if eq:
        break
    if v1 - v2 > 0:
        lo = mid
    else:
        hi = mid
    mid = (hi + lo)//2

part2 = int(mid)
print(f'Part 2: {part2}')










# import operator
# from typing import Any

# import sympy as sym


# def part_one(filename: str) -> int:
#     monkeys = parse_input(filename)
#     return int(calc_monkey_val("root", monkeys))


# def part_two(filename: str) -> int:
#     monkeys = parse_input(filename)
#     monkeys["humn"] = sym.Symbol("x")
#     m1, _, m2 = (
#         monkeys["root"].split(" ") if isinstance(monkeys["root"], str) else ("", "", "")
#     )
#     return int(
#         sym.solve(
#             calc_monkey_val(m2, monkeys) - calc_monkey_val(m1, monkeys), monkeys["humn"]
#         )[0]
#     )


# def parse_input(filename: str) -> dict[str, Any]:
#     with open(filename, encoding="utf-8") as f:
#         monkeys: dict[str, int | str] = {
#             line.strip().split(": ")[0]: line.strip().split(": ")[1]
#             for line in f.readlines()
#         }

#     for monkey, val in monkeys.items():
#         if isinstance(val, str) and len(val.split(" ")) == 1:
#             monkeys[monkey] = int(val)
#     return monkeys


# def calc_monkey_val(monkey: str, monkeys: dict) -> int | float | sym.Symbol:
#     if isinstance(monkeys[monkey], str):
#         m1, _, m2 = monkeys[monkey].split(" ")
#         match monkeys[monkey].split(" ")[1]:
#             case "+":
#                 operation = operator.add
#             case "-":
#                 operation = operator.sub
#             case "*":
#                 operation = operator.mul
#             case "/":
#                 operation = (
#                     operator.truediv
#                 )  # floordiv would be best, but sympy doesn't support it
#             case _:
#                 raise ValueError("Unknown operation")
#         monkeys[monkey] = operation(
#             calc_monkey_val(m1, monkeys), calc_monkey_val(m2, monkeys)
#         )
#     return monkeys[monkey]


# if __name__ == "__main__":
#     input_path = "Input21.txt"
#     print("---Part One---")
#     print(part_one(input_path))

#     print("---Part Two---")
#     print(part_two(input_path))


# import sys
# from z3 import Real, Solver

# class VarDict(dict):
#     def __missing__(self, key: str) -> Real:
#         self[key] = Real(key)
#         return self[key]

# def main() -> None:
#     data = sys.stdin.read().strip()

#     solver = Solver()
#     vars = VarDict()

#     for line in data.splitlines():
#         name, operation = line.split(": ")

#         if name == "humn":
#             continue

#         monkey_var = vars[name]
#         if operation.isdigit():
#             solver.add(monkey_var == int(operation))
#             continue

#         lhs, operator, rhs = operation.split(" ")
#         lhs, rhs = vars[lhs], vars[rhs]

#         if name == "root":
#             solver.add(lhs == rhs)
#             continue

#         if operator == "+":
#             solver.add(lhs + rhs == monkey_var)
#         elif operator == "-":
#             solver.add(lhs - rhs == monkey_var)
#         elif operator == "*":
#             solver.add(lhs * rhs == monkey_var)
#         else:
#             solver.add(lhs / rhs == monkey_var)

#     solver.check()
#     model = solver.model()

#     print(model[vars["humn"]].as_long())

# if __name__ == "__main__":
#     main()