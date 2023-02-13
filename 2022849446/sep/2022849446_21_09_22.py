id = 2022849446

print("Student id:", id)

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

def get_salary_breakdown(type,salary):
    switch = {
        "President":                salary_breakdown(salary, 0.7, 0.2, 0.075, 0.025),
        "Vice President":           salary_breakdown(salary, 0.7, 0.2, 0.075, 0.025), 
        "Acedemic teachings":       salary_breakdown(salary, 0.8, 0.15, 0.05), 
        "Internal affairs":         salary_breakdown(salary, 0.8, 0.15, 0.05), 
        "External affairs":         salary_breakdown(salary, 0.8, 0.15, 0.05), 
        "Research department":      salary_breakdown(salary, 0.8, 0.15, 0.05),
        "Industry department":      salary_breakdown(salary, 0.8, 0.15, 0.05),
        "Engineering department":   salary_breakdown(salary, 0.9, 0.1), 
        "Industrial engineering":   salary_breakdown(salary, 0.9, 0.1), 
    }
    return switch.get(type,"Error: Salary type does not exist")

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

def print_salary(type, salary):
    (basic, bonus, support, benefit) = get_salary_breakdown(type, salary)
    s_basic, s_bonus, s_support, s_benefit = (str(basic), str(bonus), str(support), str(benefit))
    
    (new_salary, income_tax, local_tax, insurance) = salary_breakdown_after_tax(salary)
    s_new_salary, s_income_tax, s_local_tax, s_insurance = (str(new_salary), str(income_tax), str(local_tax), str(insurance))
    
    s_currency = " WON"
    
    print()
    print("Salary breakdown for:", type)
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
        
print_salary("President", president)
print_salary("Vice President", vice_president)
print_salary("Acedemic teachings", academic_teachings)
print_salary("Internal affairs", internal_affairs)
print_salary("External affairs", external_affairs)
print_salary("Research department", research_departments)
print_salary("Industry department", industry_department)
print_salary("Engineering department", engineering_department)
print_salary("Industrial engineering", industrial_engineering)
