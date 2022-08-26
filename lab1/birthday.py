name = input("What is your name?")
birth_month = input("What month were you born?")

print(f"Hello {name}, it's nice to meet you")

if birth_month.lower() == 'august':
    print('Happy birthday month!')
    
elif birth_month.lower() == 'september':
    print('Next month is your birthday!')

else:
    print('Next month is not your birthday....')