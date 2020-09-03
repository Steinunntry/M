max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))

dollars = 0
days = 0

for i in range(max_days):
    dollars += 2**i
    if dollars >= target:
        days = i+1
        break



print('Days needed:',days)