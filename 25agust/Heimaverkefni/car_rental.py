

afram = str(input("Welcome to car rentals!\nWould you like to continue (y/n)? "))
while afram == "y" or afram == "n":
    if afram == "y":
        customer_code = str(input("Customer code (b or d): " ))
        days = float(input("Number of days: "))
        mile_start = int(input("Odometer reading at the start: "))
        mile_end = int(input("Odometer reading at the end: "))
        miles_driven = mile_end - mile_start
        print("Miles driven: ", miles_driven)
    

#grunngjöld og mílur
        b_base = float(40) #á dag
        d_base = float(60) #á dag
        mile_b = float(0.25) # á mílu
        mile_d = float(0.25) #á mílu eftir 100 mílur á dag

#forrit fyrir viðskiptavinakóða b(budget) og d(daily)
        if customer_code == "b" :
            b_base_price = b_base * days #grunngjald
            b_mile_price = mile_b * float(miles_driven) #mílur
            b_total_price = b_base_price + b_mile_price #heildarverð 
            print("Amount due:", round(b_total_price,1))

        if customer_code == "d" :
            d_base_price = d_base * days #grunngjald fyrir d 
            d_mile_price = (float(miles_driven) - (days * float(100))) * mile_d #heildar mílur reiknaðar út og svo dregnar frá 100 mílur á dag
            d_total_price = d_base_price + d_mile_price #heildarverð
            print("Amount due:", round(d_total_price,1))
    
        afram = str(input("Would you like to continue (y/n)? "))
    else :
        break