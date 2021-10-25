#Rendered a welcoming greet to a user after the initialization of the program.
print("\nWelcome to Villariza Foods! \nThe Price of an Apple is 20 PHP, while the Price of an Orange is 25 PHP.")
price_apple = 20
price_orange = 25

apple = int(input("\nPlease quantify how many apples you need to purchase... \n> Quantity: "))
orange = int(input("\nPlease quantify how many oranges you need to purchase... \n> Quantity: "))

apple_total = (apple * price_apple)
orange_total = (orange * price_orange)
grand_total = (apple_total + orange_total)

#Attached a comma feature for easy-reading numerical output.
print(f"\nThe total amount is {grand_total:,} PHP.")

