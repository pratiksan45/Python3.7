import random
win_num=random.randint(1,100)

for i in range(1,100):
    guess=int(input("Specify your number \n "))
    print("Analyzing your number..... ")
    if guess<win_num:
        print("Too Low ! ")
    elif guess>win_num:
        print("Too High ! ")
    else:
        print("CONGRATULATIONS ! Youre Number is correct")
        print(f"You guessed the winning number in {i} intervals")
        break

#names=input("Enter the Specified name\n")
#name=names.lower()
#var=""
#i=0
#while i<len(name):
    #if name[i] not in var:
        #var+=name[i]
        #print(str(name[i]) +":"+ str(name.count(name[i])  ))
    #i+=1
