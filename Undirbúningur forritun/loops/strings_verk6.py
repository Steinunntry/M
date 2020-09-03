# dæmi B

texti = "at santa at nasa"
reverse: texti[::-1]

for letter in texti:
    print(letter)




texti = input("sláðu innn texta")
val = int(input("með hvaða millibili viltu sjá stafina? "))

nýr_texti = texti[::val]