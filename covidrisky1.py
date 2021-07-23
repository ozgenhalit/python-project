age = input("Are you a cigarette addict older than 75 years old ? .....:").title() == "Yes"
print(age)
chronic = input("Do you have a severe chronic diesase?....:").title() == "Yes"
print(chronic)
immune = input("Is your immune system too weak?....:").title() == "Yes"
print(immune)
result = age or chronic or immune 
if result == True :
    print("You are in risky group. Keep your social distance and wear mask!")
else :
    print("You're not in risky group.")
