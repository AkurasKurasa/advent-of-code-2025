with open(r"day-2\given.txt") as f:
    content = f.read()

ranges = [list(map(int, item.split("-"))) for item in content.split(",")]

numbers = [num for a, b in ranges for num in range(a, b + 1)]

total = 0

for num in numbers:
    s = str(num)
    for i in range(2, len(s) + 1):
        if len(s) % i == 0 and s[:len(s) // i] * i == s:
            total += num
            break

print(total)
