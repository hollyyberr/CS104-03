#Sum & Average Program
#Holly Bernich
#s1299693

sums = []
for i in range(0,20):
    number = int(input("Enter a number: "))
    sums.append(number)
print("The sum of your 20 numbers is: ", sum(sums))
print("The average of your 20 numbers is: ", sum(sums)/len(sums))
    
    


