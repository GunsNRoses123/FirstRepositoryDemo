# Write a code to take a number as an input from the user and check if the number is odd or even.

# Step 1: tell about the program
# step 2: initialize a variable which will take input from user
# step 3: if given input number is divisible by 2, then it is an Even number.
# step 4: if not divisible by 2 then it is an odd number.
# step 5: print the final output

print("This program will check if a given number is Even or Odd!!\n")
test_number = int(input("enter your number to check!"))
if test_number % 2 == 0:
    print("test_number is even")
else:
    print("test_number is Odd")
input("\nPress any key to exit the code!")
