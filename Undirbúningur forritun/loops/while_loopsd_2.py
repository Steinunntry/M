

low = int(input("hvar byrjar bilið? "))
high= int(input("hvar endar bilið? "))

counter = low

while counter <= high:
    if counter % 2 == 1:
        print(counter)
    counter += 1