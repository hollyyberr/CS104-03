#Sum & Average Program
#Holly Bernich
#s1299693
total = 0
listNum = []
for x in range(0,20):
    number = int(input("Enter a number: "))
    listNum.append(number)
 
for x in range(0,20):
    total = total + listNum[x]
print("The sum of your 20 numbers is: ", total)
print("The average of your 20 numbers is: ", (total/len(listNum)))
