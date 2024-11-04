
# Arithmetic functions
def add(a,b):
    print(f"The sum of {a} and {b} is {a+b}")

def sub(a,b):
    print(f"The subtraction of {a} and {b} is {a-b}")

def mult(a,b):
    print(f"The multiplication of {a} and {b} is {a*b}")

def div(a,b):
    print(f"The sum division {a} and {b} is {a/b}")

#runing the program on loop taking user inputs and calling fucntions

while True:
    a = int(input("Enter the 1st Number : "))
    b = int(input("Enter the 2nd Number : "))
    c = int(input("Choose a option between 1 to 4\n[1] for Addition\n[2] for subtraction\n[3] for multiplication\n[4] for division\n[>] "))
    if c == 1:
            add(a,b) 
    elif c == 2:
            sub(a,b)
    elif c == 3:
            mult(a,b)
    elif c==4:
            div(a,b)
    else:
        print("choose a valid option")
           