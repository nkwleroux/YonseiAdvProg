print("Student id:", 2022849446)

paragraph = "My name is Nicholas. I attend Yonsei University. I am a fourth year student. My major is Computer Science. I have the class Advanced Programming. It is on monday and wednesday. It starts at 10 am. It ends at 12 pm. I eat lunch after class. Then I go to my next class."

print(paragraph[0:11] + "Alex" + paragraph[19:] + "\n")

for i in range(0, len(paragraph)):
    if(paragraph[i] == "I" and paragraph[i+1] == " "):
        paragraph = paragraph[:i] + "x" + paragraph[i+1:]
        
print(paragraph + "\n")

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
        
def main():
    
    new_titles =  [
        "student a",
        "student b",
        "student c"
    ]
    
    for (index, name) in enumerate(roles()):
        print_salary("NEW " + name[0:], index, president)
    
    for title in new_titles:
         if(title not in roles()):
            print("\nNew designation:", title)
            print("Salary breakdown for:", title)

if __name__ == "__main__":
    main()