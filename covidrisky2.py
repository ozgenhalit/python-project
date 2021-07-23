age = input("Are you a cigarette addict older than 75 years old?...:")
ageRisky = False
chronicRisky = False
immuneRisky = False
if age == "Yes" :
    ageRisky = True
chronic = input("Do you have a severe chronic diesase?....:")
if chronic == "Yes" :
    chronicRisky = True
immune = input("Is your immune system too weak?....:")
if immune == "Yes" :
    immuneRisky = True
result = immuneRisky or chronicRisky or ageRisky 
if result == True :
    print("You are in risky group. Keep your social distance and wear mask!")
else :
    print("You're not in risky group.")
