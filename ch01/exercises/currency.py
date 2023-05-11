rate = float(input("How many US Dollars per Euro?: "))
amount = float(input("How many Euros would you like to exchange?: "))
total = amount*rate
result = total-3
print("There is a $3 service fee. You will have", result, "US dollars.")