print("Welcome to the tip calculator")
bill = int(input("What was your total bill? "))
user_choice = int(input("How Much tip Would you like to give? ( 10%, 12%, 15% )"))
tip = (user_choice*bill)/100
splitting_variable= int(input("How many people Will split the bill? "))
each_person = (bill+tip)/splitting_variable
print("Each person has to pay: $", each_person)
