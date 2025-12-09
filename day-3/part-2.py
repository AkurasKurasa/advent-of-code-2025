# Not my own solution cause im fucking retarded
# Overall understand it though, RAITE 2026 im coming

banks = [line.strip() for line in open(r"day-3\given.txt")]
total = 0

for line in banks:
    bank = list(map(int, line.strip()))
    jolts = 0

    for index in range(11):
        digit = max(bank[:index - 11])
        bank = bank[bank.index(digit) + 1:]
        jolts = (jolts * 10) + digit

    jolts = (jolts * 10) + max(bank)

    total += jolts


print(total)