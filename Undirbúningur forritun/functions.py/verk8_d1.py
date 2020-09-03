
#


def mul_table(number):
    for i in range(1,11):
        print(number*i, end=" ")

#end=" " er sett til að tölurnar birtist hlið við hlið en ekki niður í röð
    



num = int(input("what line in mul table do you want"))
mul_table(num)