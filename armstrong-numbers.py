while True:
    try:
        numb = int(input("Enter a number....:"))
        if numb < 0 :
            print("Do not enter a negative number...")
            continue
    except ValueError:
        print("Do not enter a string or float. Just an Integer.")
        continue
    else :
        break
digit = str(numb)
t = 0
for i in digit:
    nume = int(i) ** len(digit) 
    t += nume
if(numb == t) :
    print("This is an Armstrong Number")
else:
    print("This is NOT an Armstrong Number.")