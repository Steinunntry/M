low = int(input("hvar byrjar bilið" ))
high = int(input("hvar endar bilið?" ))

summa_sléttra = 0

for number in range(low, high+1):
    if number % 2 == 0:
        summa_sléttra += number

print("summan er:", summa_sléttra)

#virkar rétt