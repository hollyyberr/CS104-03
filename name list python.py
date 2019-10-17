#List creation and searching
names = []
for i in range(0,10):
    n1 = input("Enter a name: ")
    names.append(n1)

keepSearching = True
while keepSearching == True:
    search = input("Enter search names:")
    if search == 'End':
        break
    if search in names:
        print(search, "the name was found")
    else:
        print(search, "the name was not found")


