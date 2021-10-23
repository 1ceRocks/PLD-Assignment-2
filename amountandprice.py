money = float(input("How much money do you have? "))
apple = float(input("What is the price of an apple per piece? "))

exchange = money % apple
apple_maxQuantity = money // apple