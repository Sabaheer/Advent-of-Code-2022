with open('Input25.txt', 'r') as file:
    data = file.read()

fuels = { '=': -2, '-': -1, '0': 0, '1': 1, '2': 2 }
decimals = dict(map(reversed, fuels.items()))

numbers = []

def to_decimal(number):
    result = sum([(5 ** ii) * fuels[c] for ii, c in enumerate(reversed(number))])
    return result

def to_fuel(number):
    value = []

    while number > 0:
        remainder = number % 5
        if remainder > 2:
            number += remainder
            value.append(decimals[remainder - 5])
        else: 
            value.append(str(remainder))

        number //= 5

    return ''.join(reversed(value))

for line in data.splitlines():
    numbers.append(to_decimal(line))

snafu = to_fuel(sum(numbers))

print('The SNAFU number to supply to the console is: ' + snafu)
















# def part_one(filename: str) -> str:
#     with open(filename, encoding="utf8") as f:
#         numbers = {line.strip() for line in f.readlines()}
#     return decimal_to_snafu(sum(snafu_to_decimal(number) for number in numbers))


# def snafu_to_decimal(snafu: str) -> int:
#     result = 0
#     for digit in snafu:
#         match digit:
#             case "2":
#                 result = result * 5 + 2
#             case "1":
#                 result = result * 5 + 1
#             case "0":
#                 result = result * 5
#             case "-":
#                 result = result * 5 - 1
#             case "=":
#                 result = result * 5 - 2
#     return result


# def decimal_to_snafu(decimal: int) -> str:
#     result = ""
#     while decimal != 0:
#         remainder = decimal % 5
#         decimal = decimal // 5
#         if remainder > 2:
#             remainder -= 5
#             decimal += 1
#         match remainder:
#             case 2:
#                 result = "2" + result
#             case 1:
#                 result = "1" + result
#             case 0:
#                 result = "0" + result
#             case -1:
#                 result = "-" + result
#             case -2:
#                 result = "=" + result
#     return result


# if __name__ == "__main__":
#     input_path = "Input25.txt"
#     print("---Part One---")
#     print(part_one(input_path))