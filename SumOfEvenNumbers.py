"""
Write a code that displays the sum of all the even numbers from the given list.
# numbers = [12, 75, 150, 180, 145, 525, 50]n%
"""

# sum of all even numbers
# use for loop since List is a sequential data structure

print("\nThis program checks all the even numbers in given list and Adds those numbers")
numbers = [12, 75, 150, 180, 145, 525, 50]
sum_even = 0
print(numbers)
for n in numbers:
    if n % 2 == 0:
        sum_even = sum_even + n
print("sum of even numbers is", sum_even)


