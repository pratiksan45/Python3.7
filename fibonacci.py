def fibonacci_seq(n):
    a=0
    b=1
    print(a, end=' ')
    print(b, end=' ')
    for i in range(1,n-1):
        c=a+b
        a=b
        b=c
        print(c, end=' ')
       

num=int(input("Enter any Number\n"))

fibonacci_seq(num)