year = int(input("Input a year: ")) # Do not change this line

# Fill in the missing code below

def hlaupaár(ártal):
    if ártal % 4 == 0:
        if ártal % 100 == 0 and ártal % 400 != 0:
            return False
        else:
            return True
    else: 
        return False


if hlaupaár(year):
    print("true")
else: 
    print("false" )