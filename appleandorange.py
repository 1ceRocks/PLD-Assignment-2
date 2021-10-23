print("The Price of Apple is 20, while the Price of Orange is 25")
price_apple = 20
price_orange = 25
apple = input("Please quantify how many apples you need to purchase: ")
orange = input("Please quantify how many oranges you need to purchase: ")

apple_string = int(apple)
orange_string = int(orange)
apple_total = (apple_string * price_apple)
orange_total = (orange_string * price_orange)
grand_total = (apple_total + orange_total)

print(f"The total amount is {grand_total}.")