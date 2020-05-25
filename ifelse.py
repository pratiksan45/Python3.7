winning_num= 50
guessed_num= int(input("Guess the winning number\n"))
if guessed_num==winning_num :
    print("\n YOU Win !!")
else:
    if guessed_num > winning_num:
       print("\n Too High !!")
    else:
        print("\n Too Low !! ")
