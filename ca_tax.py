#Setting global tax rates per Canadian Province
on = 0.13
ab = 0.05
bc = 0.12
qc = 0.1498
sk = 0.11
nb = 0.15
#Create tax function that takes price and tax_rate as imputs and returns the total price
def calculate_tax(price, tax_rate):
    total = price + (price * tax_rate)
    total = round(total, 2) #round it to 2 decimal places
    return total
#Explain the program
print ('This is a Canadian tax calculator.\nEnter in the price of your item and the program will calculate how much it costs with tax.\n')
#Ask user to input province
province = input("Please select the tax code (i.e. on): \n on - Ontario \n ab - Alberta \n bc - British Columbia \n qc - Quebec \n sk - Saskatchewan \n nb - New Brunswick \n: ")
if province == 'on':
    my_price = float(input("Price $"))
    my_price_with_tax = calculate_tax(my_price, on)
    print ('The price with tax: $', my_price_with_tax)
elif province == 'ab':
    my_price = float(input("Price $"))
    my_price_with_tax = calculate_tax(my_price, ab)
    print ('The price with tax: $', my_price_with_tax)
elif province == 'bc':
    my_price = float(input("Price $"))
    my_price_with_tax = calculate_tax(my_price, bc)
    print ('The price with tax: $', my_price_with_tax)
elif province == 'qc':
    my_price = float(input("Price $"))
    my_price_with_tax = calculate_tax(my_price, qc)
    print ('The price with tax: $', my_price_with_tax)
elif province == 'sk':
    my_price = float(input("Price $"))
    my_price_with_tax = calculate_tax(my_price, sk)
    print ('The price with tax: $', my_price_with_tax)
elif province == 'nb':
    my_price = float(input("Price $"))
    my_price_with_tax = calculate_tax(my_price, nb)
    print ('The price with tax: $', my_price_with_tax)
else:
    print ("You did not choose a a correct province code")