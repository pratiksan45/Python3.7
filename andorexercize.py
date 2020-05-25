name,age=input("Enter your Name and Age\n").split( )
if name[0].lower()=='a' and int(age)>=18:
    print("You can watch This Movie")
else:
    print("You cannot Watch this Movie")