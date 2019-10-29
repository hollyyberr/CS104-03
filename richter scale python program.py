#Richter Scale
#Name: Holly Bernich
#ID: s1299693

scale = True

while scale == True:
    richter = float(input("Enter a Richter value: (Enter '-99' to exit program)"))
    if richter == -99:
        break
    while richter < 0:
        richter = float(input("Enter a new value greater than zero."))
    if richter >= 8.0:
            print("Most structures fall.")
    elif richter >= 7.0:
            print("Many buldings destroyed.")
    elif richter >= 6.0:
            print("Many buildings considerably damaged, some collapse.")
    elif richter >= 4.5:
            print("Damage to poorly constructed buildings.")
     else:
            print("No destruction of buildings.")
            
