print("[CALCULATOR 2024]")
print("   ")
print("   ")
print("   ")

str(print("ENTER FIRST NUMBER: "))
Num1 = int(input())

str(print("ENTER OPERATION TO BE PERFORMED: "))
Op = str(input())

str(print("ENTER SECOND NUMBER "))
Num2 = int(input())
 
Result = 0
                                                 
def ADD():
   Result = Num1 + Num2
   print(Result)

def SUBTRACT():
    Result = Num1 - Num2
    print(Result)

def MULTIPLY():
    Result = Num1 * Num2
    print(Result)

def DIVIDE():
     Result = Num1 / Num2
     print(Result)

if Op == "+":
   ADD()

elif Op == "-":
     SUBTRACT()

elif Op == "*":
     MULTIPLY()

elif Op == "/":
     DIVIDE()
     
else:
    print("ERROR!!! PLEASE TRY AGAIN...")


