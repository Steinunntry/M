#loops dæmi 3
low = int(input("hvar byrjar bilið? "))
high = int(input("hvar endar bilið? "))

summa = 0

for number in range(low,high+1):
    summa += number

print("summan er: ",summa)
