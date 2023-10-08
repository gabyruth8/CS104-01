#CS104
#GabriellaVelasquez
#Conditions.py
temp= int("100")
while temp!= "end":
    temp= int(input("Please enter the current temperature:"))
    if temp>= 90:
        print("Wear shorts")
    elif temp>= 70:
        print("Short sleeves are fine")
    elif temp>= 50:
        print("Weat a heavy coat")
    else:
        print("Stay Inside")
