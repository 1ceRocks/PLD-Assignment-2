#Rendered a welcoming greet to a user after the initialization of the program.
print("\nWelcome to Villariza Foods! Our available product for today is apple. \n")
money = float(input("How much cash do you possess right now? \n> PHP: "))
apple = float(input("\nWhat is the cost of an apple per item? \n> PHP: "))

#Displayed an aditional feature and response when a user does not have enough money to buy a single quantity of Apple.
if money >= apple:
    exchange = money % apple
    apple_maxQuantity = int(money // apple)
    print(f"\nYou can buy {apple_maxQuantity} apples and your change is {exchange: .2f} PHP.")
else:
    moneyShortage = float(apple - money)
    print(f"\nSorry, but you do not have enough money to buy an apple. You need {moneyShortage: .2f} PHP in order to purchase a single apple.")