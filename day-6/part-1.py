lines = [line.strip().split() for line in open(r"day-6\given.txt")]
cols = list(zip(*lines))

total = 0

for *nums, op in cols:
    total += eval(op.join(nums))

print(total)