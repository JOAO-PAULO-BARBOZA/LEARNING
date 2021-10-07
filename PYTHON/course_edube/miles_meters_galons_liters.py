def liters_100km_to_miles_gallon(liters):
    miles = 100 / 1.609344
    gallon = liters / 3.785411784
    res = miles / gallon
    return res


def miles_gallon_to_liters_100km(miles):
    km = (miles * 1.609344)/100
    liters = 3.785411784

    res = liters / km
    return res


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
