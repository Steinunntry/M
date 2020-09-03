#hlaupaár

#ártal er færibreyta

def hlaupaár(ártal):
    if ártal % 4 == 0:
        if ártal % 100 == 0 and ártal % 400 != 0:
            return False
        else:
            return True
    else: 
        return False


ár = int(input("sláðu inn ártal og ég skal finnn út hvort að það sér hlaupaár eða ekki. "))
if hlaupaár(ár):
    print("hlaupaár")
else: 
    print("Ekki hlaupaár." )
