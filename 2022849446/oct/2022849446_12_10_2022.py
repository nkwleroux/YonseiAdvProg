import math
import os.path 
import csv

print("Student id:", 2022849446)

#random funcitons
def fun1():
    print("fun1")

def fun2():
    print("fun2")
    
def fun3():
    print("fun3")
    
def fun4():
    print("fun4")

def fun5():
    print("fun5")

def callFunction(functionName):
    print("Function called: ")
    if(functionName == "fun1"):
        fun1()
    elif(functionName == "fun2"):
        fun2()
    elif(functionName == "fun3"):
        fun3()
    elif(functionName == "fun4"):
        fun4()
    elif(functionName == "fun5"):
        fun5()
    elif(functionName == "exit"):
        exit()
    else:
        print("not found")

def menu():
    print("Menu:")
    print("1. fun1")
    print("2. fun2")
    print("3. fun3")
    print("4. fun4")
    print("5. fun5")
    print("6. Exit")

menu()             
print("Select a function to call:")
fName = input()
callFunction(fName)

def sumInfLoop(breakpoint):
    num = 0
    while True:
        num += 1
        if(num == breakpoint):
            break

    print("Function - sumInfLoop result", num)
    return num

sumInfLoop(10)

def sumFiniteLoop(continuepoint,breakpoint):
    num = 0
    while True:
        num += 1
        if(num == continuepoint):
            continue
        if(num == breakpoint):
            break

    print("Function - sumFiniteLoop result", num)
    return num

sumFiniteLoop(5,10)

def iterationExampleFromWhiteBoard(num, iterations):
    res = 0
    while(iterations > 0):
        if(iterations == 1):
            res += num
        else:
            res += math.pow(num,iterations)
        
        iterations = iterations - 1
        
    print("Function - iterationExampleFromWhiteBoard result", res)        
    return res

iterationExampleFromWhiteBoard(2,3)

path = "./python/2022849446/oct/names.csv"
file_exists = os.path.exists(path)    
if(file_exists == False): 
    
    names = ["Alex, Tony, Jessica, Juliet, Max, John, Jane, Mark, Mary, James"]
    
    with open(path,'w') as f:
        write = csv.writer(f)
        write.writerow(["Names: ", names])
else:
    
    with open(path,'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if(len(row) > 0 ):   
                print(row[1])
