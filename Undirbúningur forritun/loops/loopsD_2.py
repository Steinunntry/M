#dæmi 2 í loops
low = int(input("hvar byrjar bilið"))
high = int(input("hvar endar bilið?"))

for tala in range(low,high+1,1):
    if tala % 2 == 1:
        print(tala)