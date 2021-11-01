print("Currency Convertor - Convert INR to any currency")

#Opening file - currency.txt

with open("currency.txt") as f:
    lines = f.readlines()

# print(lines)
currencyDict = {}
for line in lines:
    parsed= line.split("\t")#You can ignore the newline character
    # print(parsed)#It is a list
    currencyDict[parsed[0]] = parsed[1]#parsed[1] is the conversion rate which can be mulitplied to any value of INR

# print(currencyDict)
amount = int(input("Enter the amount of INR:\n"))
print("Enter the name of currency in which you want to convert\nAvailable options are")
# li = [item for item in currencyDict.keys()]
# for item in li:
#     print(item)
"""ShortForm or above code"""
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of these values:\n")
print(f"{amount} INR is equal to {float(currencyDict[currency] )* amount } {currency}")