# Ask name and birth month
name = input("What is your name? ")
birth_month = input("What month were you born? ")

# greet, with name, and numbert of letters in name
print(f"Hello {name.capitalize()}, it's nice to meet you.")
print(f"There are {len(name)} letters in your name and ")

if birth_month.lower() == "august":
    print("it's your birthday month!")

elif birth_month.lower() == "september":
    print("next month is your birthday!")

else:
    print("next month is not your birthday....")
