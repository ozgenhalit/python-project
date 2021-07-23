left = ["q","w","e","r","t","a","s","d","f","g","z","x","c","v","b"]
right = ["p","o","ı","u","i","l","k","j","m","n"]
kelime = input("Bir kelime girin...:")
rightTrack = False
leftTrack = False
for i in kelime :
    if i in left:
        leftTrack = True
    elif i in right:
        rightTrack = True
print(rightTrack and leftTrack)
