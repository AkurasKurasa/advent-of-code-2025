turns = [int(line.strip().replace("L", "-").replace("R", "")) for line in open(r"day-1\given.txt")]
dial = 50
count = 0

def secretEntrance(turn, num):
    pass

for turn in turns:
    dial = (dial + turn) % 100
    if dial == 0: count += 1

print(count)