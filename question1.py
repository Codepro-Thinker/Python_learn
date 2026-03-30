def calculate_tax(basic_pay):
    if basic_pay <= 20000:
        tax_rate = 0
    elif basic_pay <= 25000:
        tax_rate = 10
    elif basic_pay <= 30000:
        tax_rate = 15
    else:
        tax_rate = 20
    tax_amount = (tax_rate / 100) * basic_pay
    return tax_rate, tax_amount

def print_payslip(emp_code, name, designation, department, basic_pay):
    tax_rate, tax_amount = calculate_tax(basic_pay)
    net_salary = basic_pay - tax_amount

    print("\n" + "="*40)
    print(" "*10 + "EMPLOYEE PAYSLIP")
    print("="*40)
    print(f"Employee Code : {emp_code}")
    print(f"Name          : {name}")
    print(f"Designation   : {designation}")
    print(f"Department    : {department}")
    print("-"*40)
    print(f"Basic Pay     : ₹{basic_pay:,.2f}")
    print(f"Tax Rate      : {tax_rate}%")
    print(f"Tax Amount    : ₹{tax_amount:,.2f}")
    print(f"Net Salary    : ₹{net_salary:,.2f}")
    print("="*40)

emp_code = input("Enter Employee Code: ")
name = input("Enter Employee Name: ")
designation = input("Enter Designation: ")
department = input("Enter Department: ")
basic_pay = float(input("Enter Basic Pay: "))

print_payslip(emp_code, name, designation, department, basic_pay)