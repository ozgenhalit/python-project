from datetime import date
birth = date(1881, 1, 1)
death = date(1938, 10, 10)
life_in_days = date.toordinal(death)- date.toordinal(birth)
print(life_in_days)
