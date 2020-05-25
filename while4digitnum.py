num=input("Enter any digit number \n")
i = 0
total=0
while i<len(num):
    total+=int(num[i])
    i+=1
print(f"Total Sum of number is {total}")