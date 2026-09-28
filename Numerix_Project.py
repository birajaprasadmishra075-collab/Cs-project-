ap=["+","-","*","/","//","%","**"]
TP=["sin(A)","cos(A)","tan(A)"]
FT=["C!"]
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
n=70
for i in range(n):
    print("=",end="")
print("\n           Numerix: An Algorithmic Scientific Calculator Engine\n                    Analytics Engine - Main Menu")
n=70
for i in range(n):
    print("=",end="")
while True:    
    print("\nWelcome! Would you like to perform a calculation?")
    your_answer=input("Please answer the above question in \"yes\" or \"no\":")
    if your_answer=="yes":
        print("\nSelect a category of operations:")
        print(" 1. Arithmetic   : +, -, *, /, //, %, **")
        print(" 2. Trigonometry : sin(A), cos(A), tan(A)")
        print(" 3. Factorial    : C!")
        operator=input("Enter the operater you want to use:")
        if operator in ap:
            A=float(input("Enter the first no.  :"))
            B=float(input("Enter the second no. :"))
            D= operator
            if D=='+':
               print("Result:",A+B)
            elif D=='-':
                 print("Result:",A-B)
            elif D=='*':
                 print("Result:",A*B)
            elif D=='//':
                print(A//B)
            elif D=='%':
                print("Result:",A%B)
            elif D=='**':
                print("Result:",A**B)
            elif D=='/':
                 if B!=0:
                    print("Result:",A/B)
                 else :
                    print("Undefined (division by zero).")
            else :
                print("Invalid operator selected.")
        elif operator in TP:
            A=int(input(" Enter the angle(you are only allowed to use {0,30,45,60,90}):"))
            S=operator
            if S=="sin(A)":
                if A==0:
                   print("Result:0")
                elif A==30:
                    print("Result:1/2")
                elif A==45:
                    print("Result:1/(2**0.5)")
                elif A==60:
                   print("Result:(3**0.5)/2")
                elif A==90:
                    print("Result:1")
                else:
                    print("You are only allowed to select from the six basic valus like(0,30,45,60,90)")
            elif S=="cos(A)":
                if A==0:
                   print("Result:1")
                elif A==30:
                    print("Result:(3**0.5)/2")
                elif A==45:
                    print("Result:1/(2**0.5)")
                elif A==60:
                   print("Result:1/2")
                elif A==90:
                    print("Result:0")
                else:
                    print("You are only allowed to select from the six basic valus like(0,30,45,60,90)")
            elif  S=="tan(A)":
                if A==0:
                   print("Result:0")
                elif A==30:
                    print("Result:1/(3**0.5)")
                elif A==45:
                    print("Result:1")
                elif A==60:
                   print("Result:3**0.5")
                elif A==90:
                    print("Result:Not defined(infinity)")
                else:
                    print("You are only allowed to select from the six basic valus like(0,30,45,60,90)")      
            else:
                print("Your operator is not in the given list")      
        elif operator in FT:
            n=int(input("Enter the no. :"))
            print("Result:",fact(n))  
        else:
            print("Invalid operator")
        print("                       Thank you for using Numerix")
        n=70
        for i in range(n):
            print("=",end="")
    else:
        print("                       Thank you for using Numerix")
        n=70
        for i in range(n):
            print("=",end="")
        break
