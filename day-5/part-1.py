ranges, numbers = open(r"day-5\given.txt").read().split("\n\n")

ranges = [list(map(int, r.split("-"))) for r in ranges.splitlines()]
numbers = list(map(int, numbers.splitlines()))

count = 0

for number in numbers:
    for low, high in ranges:
        if low <= number <= high:
            count += 1
            break

print(count)
