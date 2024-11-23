# Function to calculate the tax based on the rules
def calculate_tax(salary):
    tax = 0
    if salary <= 500000:
        tax = 0  # No tax for salary <= 5 Lac
    elif salary <= 750000:
        tax = (salary - 500000) * 0.05  # 5% tax for 5-7.5 Lac
    elif salary <= 1000000:
        tax = (salary - 750000) * 0.10 + (250000 * 0.05)  # 10% tax for 7.5-10 Lac
    elif salary <= 10000000:
        tax = (salary - 1000000) * 0.15 + (250000 * 0.10) + (250000 * 0.05)  # 15% tax for 10-12.5 Lac
    else:
        tax = (salary - 10000000) * 0.20 + (250000 * 0.15) + (250000 * 0.10) + (250000 * 0.05)  # 20% tax for salary above 10 Lac
    return tax

# Input file path
input_file = 'employee_details.txt'
output_file = 'tax_output.txt'

# Dictionary to store employee ID and the corresponding tax
tax_dict = {}

# Reading the input file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Processing each line (employee details)
for line in lines:
    details = line.strip().split(',')
    name = details[0]
    employee_id = details[1]
    gross_salary = float(details[2])
    provident_fund = float(details[3])
    advance_tax = float(details[4])

    # Calculating the net salary and tax
    net_salary = gross_salary - provident_fund - advance_tax
    tax_to_be_deposited = calculate_tax(net_salary)

    # Storing the tax in the dictionary
    tax_dict[employee_id] = tax_to_be_deposited

    # Writing to output file
    with open(output_file, 'a') as outfile:
        outfile.write(f"Name: {name}; ID: {employee_id}; Tax: {tax_to_be_deposited:.2f}\n")

# Printing the dictionary to show the result
print("Employee Tax Details:")
for employee_id, tax in tax_dict.items():
    print(f"ID: {employee_id}, Tax: {tax:.2f}")
