#Verkefni 2 "where is Voyager 1?" bls 115

#Hvað ferðast Voyager margar mílur á einum degi? 
#hraði 38241 m/h tími 24 h (vegalengd = hraði * tími)
day_1_miles = 38241 * 24

#breyta miles í AU og KM
km_to_miles = 1.609344 
AU_to_miles = 92955887.6

# finna AU og KM á einum degi
day_1_km = day_1_miles * km_to_miles
day_1_AU = day_1_miles / AU_to_miles

#fjarlægðir frá sólu í AU og KM
miles_from_sun = 16637000000
km_from_sun = miles_from_sun * km_to_miles
AU_from_sun = miles_from_sun / AU_to_miles

days = int(input ("Number of days after 9/25/09: "))


distance_m = miles_from_sun + (day_1_miles * days)
distance_k = km_from_sun + (day_1_km * days)
distance_AU = AU_from_sun + (day_1_AU * days)

print("Miles from the sun:", distance_m)
print("Kilometers from the sun:", round(distance_k))
print("AU from the sun:", round(distance_AU))

