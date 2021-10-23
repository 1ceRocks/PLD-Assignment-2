money = float(input("How much cash do you possess right now? "))
apple = float(input("What is the cost of an apple per item? "))

exchange = money % apple
apple_maxQuantity = money // apple

print(f"You can buy {apple_maxQuantity: .2f} apples and your change is {exchange: .2f}.")