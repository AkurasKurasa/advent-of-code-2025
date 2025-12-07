IDs = [item for line in open(r"day-2\given.txt") for item in line.strip("\n").split(",")]

sum = 0

for id in IDs:
    start, end = id.split("-")
    
    for num in range(int(start), int(end)):

        num = str(num)

        if num[len(num) // 2:] == num[:len(num) // 2]:
            sum += int(num)

print(sum)

# THE CODE IS SO FCKING ASSSSS