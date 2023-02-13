from math import sqrt, radians, sin, cos, atan2

#####################
###### TASK  1 ######
#####################

#10 Designations
# 1. President
# 2. Vice President
# 3. Acedemic teachings
# 4. Internal affairs
# 5. External affairs
# 6. Research department
# 7. Industry department
# 8. Engineering department
# 9. Industrial engineering
# 10 Students

#Variables in WON
president = 2500000 #2.5 mil
vice_president = 2000000 #2 mil
academic_teachings = 900000 #900k
internal_affairs = 800000 #800k
external_affairs = 700000 #700k
research_departments = 600000 #600k
industry_department = 500000 #500k
engineering_department = 400000 #400k
industrial_engineering = 250000 #250k

def roles():
    return [
    "President",              
    "Vice President",     
    "Acedemic teachings",     
    "Internal affairs",       
    "External affairs",    
    "Research department",    
    "Industry department", 
    "Engineering department", 
    "Industrial engineering",
    ]
    
def salary():
    return [
        2500000,    #2.5 mil    "President",              
        2000000,    #2 mil      "Vice President",     
        900000,     #900k       "Acedemic teachings",     
        800000,     #800k       "Internal affairs",       
        700000,     #700k       "External affairs",    
        600000,     #600k       "Research department",    
        500000,     #500k       "Industry department", 
        400000,     #400k       "Engineering department", 
        250000,     #250k       "Industrial engineering",
    ]

def get_salary_breakdown_dict(type,salary):
    switch = {
        roles()[0]: salary_breakdown(salary, 0.7, 0.2, 0.075, 0.025),
        roles()[1]: salary_breakdown(salary, 0.7, 0.2, 0.075, 0.025), 
        roles()[2]: salary_breakdown(salary, 0.8, 0.15, 0.05), 
        roles()[3]: salary_breakdown(salary, 0.8, 0.15, 0.05), 
        roles()[4]: salary_breakdown(salary, 0.8, 0.15, 0.05), 
        roles()[5]: salary_breakdown(salary, 0.8, 0.15, 0.05),
        roles()[6]: salary_breakdown(salary, 0.8, 0.15, 0.05),
        roles()[7]: salary_breakdown(salary, 0.9, 0.1), 
        roles()[8]: salary_breakdown(salary, 0.9, 0.1), 
    }
    return switch.get(type,"Error: Salary type does not exist")

def roles_dict():
    roles_dict = dict()
    
    for (index, name) in enumerate(roles()):
        salary_breakdown = get_salary_breakdown_list(index, president)
        roles_dict[name] = salary_breakdown[1]
    
    return roles_dict
    
def get_salary_breakdown_list(index,salary):
    return roles()[index], get_salary_breakdown_dict(roles()[index],salary)

def salary_breakdown(salary, basic_percent, bonus_percent, support_percent = 0, benefit_percent = 0):
    basic = salary * basic_percent
    bonus = salary * bonus_percent
    support = salary * support_percent
    benefit = salary * benefit_percent
    return basic, bonus, support, benefit

def salary_breakdown_after_tax(salary):
    income_tax = salary * 0.1
    local_tax = salary * 0.05
    insurance = salary * 0.02
    new_salary = salary - income_tax - local_tax - insurance
    return new_salary, income_tax, local_tax, insurance

def print_salary(name,salary_level,salary):
    print("\nSalary breakdown for:", name)
    return print_salary_calculation(salary_level, salary)    

def print_salary_calculation(type, salary):
    if(get_salary_breakdown_dict(str(type), salary) != "Error: Salary type does not exist"):
        (basic, bonus, support, benefit) = get_salary_breakdown_dict(str(type), salary)
    else:
        (type, (basic, bonus, support, benefit)) = get_salary_breakdown_list(type, salary)
    s_basic, s_bonus, s_support, s_benefit = (str(basic), str(bonus), str(support), str(benefit))
    
    (new_salary, income_tax, local_tax, insurance) = salary_breakdown_after_tax(salary)
    s_new_salary, s_income_tax, s_local_tax, s_insurance = (str(new_salary), str(income_tax), str(local_tax), str(insurance))
    
    s_currency = " WON"

    total_salary_before_tax = "Total salary before tax: " + str(salary) + s_currency
    total_salary_before_tax += " (Basic: " + s_basic + s_currency + ", "
    total_salary_before_tax += "Bonus: " + s_bonus + s_currency
    
    if(support > 0):
        total_salary_before_tax += ", Support: " + s_support + s_currency
    if(benefit > 0):
        total_salary_before_tax += ", Benefit: " + s_benefit + s_currency
    
    total_salary_before_tax += ")"
    print(total_salary_before_tax)
    
    total_salary_after_tax = "Total salary after tax: " + s_new_salary + s_currency
    total_salary_after_tax += " (Income tax: " + s_income_tax + s_currency
    total_salary_after_tax += ", Local tax: " + s_local_tax + s_currency
    total_salary_after_tax += ", Insurance: " + s_insurance + s_currency + ")"
    print(total_salary_after_tax)
        
def task1():
    
    roles = roles_dict()
    print(roles)
    
    president_salary = get_salary_breakdown_dict("President", president)
    print(president_salary)
    
#####################
###### TASK  2 ######
#####################
earthRadius = 6378.137 #in km

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
    return earthRadius * c # in km

def task2():
    SeoulTuple = (37.566, 126.9784)
    BusanTuple = (35.10168, 129.03004)

    distance = distanceBetweenCoordsTuple(SeoulTuple,BusanTuple)
    arcDistance = arcDistanceBetweenCoordsTuple(SeoulTuple,BusanTuple)

    print("The coordinates of Seoul is", SeoulTuple, ". The coordinates of Busan is", BusanTuple, ".")
    print("The point of symmetry/middle point is", pointOfSymmetry(SeoulTuple,BusanTuple))
    print("The distance between Seoul and Busan is (Euclidean):", distance,"km")
    print("The distance to the middle point is (Euclidean):", distance/2,"km")
    print("The distance between Seoul and Busan is (Arc/Haversine formula):", arcDistance,"km")
    print("The distance to the middle point is (Arc/Haversine formula):", arcDistance/2,"km")

if __name__ == "__main__":
    
    print("Student id is:", 2022849446)

    task1()
    task2()
    