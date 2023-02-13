from math import sqrt, radians, sin, cos, atan2

print("Student id is:", 2022849446)

### Quesition 1 ###

def pointOfSymmetry(coord1,coord2):
    return ((coord1[0]+coord2[0])/2,(coord1[1]+coord2[1])/2)

def distanceBetweenCoordsTuple(coord1,coord2):
    return sqrt(pow(coord2[0]-coord1[0],2)+pow(coord2[1]-coord1[1],2))

def arcDistanceBetweenCoordsTuple(coord1,coord2):
    
    lat1 = radians(coord1[0])
    lat2 = radians(coord2[0])
    
    dLat = radians(coord2[0]-coord1[0])
    dLong = radians(coord2[1]-coord1[1])

    #Haversine formula found online at https://www.movable-type.co.uk/scripts/latlong.html
    a = sin(dLat/2) * sin(dLat/2) + cos(lat1) * cos(lat2) * sin(dLong/2) * sin(dLong/2)
    
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    earthRadius = 6378.137 #in km
    return earthRadius * c # in km

def question1():
    
    YonseiUniCoordinates = (37.5657, 126.9386)
    KoreaUniCoordinates = (37.5907, 127.0275)
    
    middlePoint = pointOfSymmetry(YonseiUniCoordinates,KoreaUniCoordinates)
    distance = distanceBetweenCoordsTuple(YonseiUniCoordinates,KoreaUniCoordinates)
    arcDistance = arcDistanceBetweenCoordsTuple(YonseiUniCoordinates,KoreaUniCoordinates)

    # print("The coordinates of Seoul is", YonseiUniCoordinates, ". The coordinates of Busan is", KoreaUniCoordinates, ".")
    print(middlePoint)
    print("Euclidean:", distance)
    print("Arc/Haversine formula:", arcDistance)
    print("middle point (Euclidean):", distance/2)
    print("middle point (Arc/Haversine formula):", arcDistance/2)
    
### Question 2 ###    

def calculate_salary(desig):
    salary = 0
    des = desig[0:].lower()
    basic = 20000
    bonus = 15000
    sup_1 = 13000
    sup_2 = 10000
    sup_3 = 8000
    sup_4 = 5000
    sup_5 = 2000
    
    if(des == "president"):
        salary = (basic * 1.00) + bonus + sup_1 + sup_2 + sup_3 + sup_4 + sup_5
    elif(des == "vice president"):
        salary = (basic * 0.95) + bonus + sup_1 + sup_2 + sup_3 + sup_4
    elif(des == "acedemic teachings"):
        salary = (basic * 0.90) + bonus + sup_1 + sup_2 + sup_3
    elif(des == "internal affairs"):
        salary = (basic * 0.85) + bonus + sup_1 + sup_2 + sup_3
    elif(des == "external affairs"):
        salary = (basic * 0.80) + bonus + sup_1 + sup_2 + sup_3
    elif(des == "research departments"):
        salary = (basic * 0.75) + bonus + sup_1 + sup_2
    elif(des == "industry department"):
        salary = (basic * 0.70) + bonus + sup_1 + sup_2
    elif(des == "engineering department"):
        salary = (basic * 0.65) + bonus + sup_1
    elif(des == "industrial engineering"):
        salary = (basic * 0.60) + bonus + sup_1
    elif(des == "students"):
        salary = (basic * 0.55) + bonus
    else:
        pass
    
    return salary
    
def changeDesignation(old,new):
    if("vice" in new and "vice" not in old):
        return new[0:] + old[0:]
    else:
        return new[0:]

def printSalary(des, sal):
    print(des, "salary:", sal)
       
def question2():
    
    designation = "president"
    salary = calculate_salary(designation)
    printSalary(designation,salary)
    
    designation = changeDesignation(designation,"vice ")
    salary = calculate_salary(designation)
    printSalary(designation,salary)
    
    designation = "acedemic teachings"
    salary = calculate_salary(designation)
    printSalary(designation,salary)
    
    designation = "internal affairs"
    salary = calculate_salary(designation)
    printSalary(designation,salary)
    
    designation = "external affairs"
    salary = calculate_salary(designation)
    printSalary(designation,salary)
    
    designation = "research departments"
    salary = calculate_salary(designation)
    printSalary(designation,salary)
    
    designation = "industry department"
    salary = calculate_salary(designation)
    printSalary(designation,salary)
    
    designation = "engineering department"
    salary = calculate_salary(designation)
    printSalary(designation,salary)
    
    designation = "industrial engineering"
    salary = calculate_salary(designation)
    printSalary(designation,salary)
    
    designation = "students"
    salary = calculate_salary(designation)
    printSalary(designation,salary)

### main ###
    
def main():
    # question1() 
    question2()


if __name__ == "__main__":
    main()

