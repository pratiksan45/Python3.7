
names=input("Enter the Specified name\n")
name=names.lower()
var=""
i=0
while i<len(name):
    if name[i] not in var:
        var+=name[i]
        print(str(name[i]) +":"+ str(name.count(name[i])  ))
    i+=1