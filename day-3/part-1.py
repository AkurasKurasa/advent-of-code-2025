banks = [line.strip() for line in open(r"day-3\given.txt")]

# Digits left = 12


ptrL = 0
ptrR = 1

sum = 0

for bank in banks:
    maximum = 0
    ptrL = 0
    ptrR = 1

    while ptrL <= len(bank) - 1 and ptrR <= len(bank) - 1:

        maximum = max(maximum, int(bank[ptrL] + bank[ptrR]))

        if bank[ptrL] < bank[ptrR]:
            ptrL = ptrR

        ptrR += 1

    sum += int(maximum)

print(sum)

# If youre reading this I know the code is shit, ik you are; stfu.
# Own solution but dogass; fuck me though.