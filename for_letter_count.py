name=input("Enter the string\n")
var=""
for i in range(0,len(name)):
    if name[i] not in var:
        var+=name[i]
        print(f"{name[i]} : {name.count(name[i])}")