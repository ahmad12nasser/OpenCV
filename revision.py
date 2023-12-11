# The tax fees must be applied based on the data given in following table:
# Shipment Amount in $ Custom fees in $
# <=1000 50
# >1000 and <=2000 10%
# >2000 and <=3000 12%
# >3000 14%
#
# That is, when the total shippment amount is less than 1000$, then there will be 50$
# tax fees to apply. When the total shipment amount is greater than 1000$ and less than
# or equal to 2000$, then there will be 10% custom tax fees to apply, and so on.
#
# Sample Run 1:
# Enter the Total Amount of Shipment: 500.0
# Your custom fees is 50.0$
# You have to pay a total of 500.0+50.0 = 550.0$

def getbonus(salary):
    if salary <=1000:
        bonus = 50
    elif salary <=2000:
        bonus = salary * 0.1
    elif salary <=3000:
        bonus = salary * 0.12
    else:
        bonus = salary * 0.14
    return bonus
def getNewSalary(salary,bonus):
    return salary + bonus

salary = input("Enter the total amount of the shippment: ")

try:
    salary = float(salary)
    custom_fees = getbonus(salary)
    total = getNewSalary(salary,custom_fees)

    print("your custom fees is {} $".format(custom_fees))
    print("you have to pay a total {} + {} = {}".format(salary,custom_fees,total))

except ValueError:
    print("Enter a number")
