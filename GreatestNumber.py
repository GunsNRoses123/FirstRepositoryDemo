# Write a code to take 3 numbers as an input from the user and display the greatest no as output.

# take 3 inputs from user
# check if num1 > then num2 , and num1 > num3, then print num 1
# check if num2 > then num3 , and num2 > num1, then print num 2
# else print num3

first_num = int(input("\nEnter your first number!"))
second_num = int(input("\nEnter your second number!"))
third_num = int(input("\nEnter your third number!"))
if first_num > second_num and first_num > third_num:
    print("Greatest number is", first_num)
elif second_num > third_num and second_num > first_num:
    print("Greatest number is", second_num)
else:
    print("Greatest number is", third_num)
input("\nPress any key to exit!")

# another way of doing this can be using a list and in built Math function i.e. MAX()22
# for example list1 = [213,123,300]
# print = max(list1)
# we will get 300 as maximum or greatest number in the list.