#Arranged the variables and the spacing between the input function for easy viewing.
print("\nYour Personal Information")
userName = input("\nEnter your NAME here. \n> ")
userAge = int(input("\nEnter your AGE here in numbers. \n> "))
userAddress = input("\nEnter your ADDRESS here. \n> ")

#Annexed an additional print response acting as a comment on a user input.
print("\nPython has inputted your personal information.")
print(f"\nHi, my name is {userName}. I am{userAge: .0f} years old and I live in {userAddress}.")