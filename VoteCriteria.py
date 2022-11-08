# Write a code to take the age of person as an input and if age >= 18 display "I can vote". I
# f age is < 18 display "I can't vote".

# explain the program
# initialize a variable that will take input from user. This variable will hold Age criteria value.
# if age >= 18, then a Person is allowed to vote.
# if age < 18, then a person is not allowed to vote.
# print the message
# exit the program

print("\nWelcome to the Biggest Democratic event of the world")
print("\nYou have the privilege and power to choose the Candidate of your choice")
print("\nUse your Vote with wisdom and thinking because future of the country is in your hands")
print("\nBut first we have to check whether you are eligible to take part in this humongous process!")
vote_age = int(input("enter your age to check!"))
if vote_age >= 18:
    print("Yes! you will be part of the biggest Voting event")
elif vote_age < 18:
    print("Sorry! you are still a child :(")
print("\nAlways remember , country comes first! ")
input("\nPress any key to exit!")


