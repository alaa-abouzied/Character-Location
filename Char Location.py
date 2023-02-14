str = input("enter ur string: ")
i = 0
for index, item in enumerate(str):
    if item == 'i':
        print(str ,"has 'i' in index: ",index)
        i += 1

if i == 0:
    print(str, " has zero 'i'")
