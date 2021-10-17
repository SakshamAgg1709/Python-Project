# Write a Python Program which will keep adding a stream of numbers inputed  by the user. The adding stops as soon as user presses q on his keyboard

print("Welcome to our shop. \nPlease enter the price of the commodities one by one followed by a enter key\nPress q for quittin the calculation process")
sum = 0 
li = []
while(True):
    userInput = input("Enter the price :\n")

    if userInput != 'q':
        li.append(userInput)
        sum = sum + int(userInput)
        print(f"Order Total so far : {sum}")
    else:
        print(f"This is your reciept, Thanks for shopping with us")
        for i in li:
            print(i)
        print(f"Sum Total: {sum}")
        break

