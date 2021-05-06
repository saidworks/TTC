from matplotlib.pyplot import plot, axis, show, legend

mortgage_amount = float(input("How much is the mortgage for?"))
interest_rate = float(input("What is the interest rate (as a percentage)?"))/100
payment = float(input("How much are you paying per month?"))

max_months = 1200 # don't figure for more than 10 years
month = 0
month_list = [0]
mortgage_list = [mortgage_amount]
principal_paid_list = [0]
interest_paid_list = [0]

while (mortgage_amount > 0.0) and (month < max_months):
    month += 1
    month_list.append(month)
    #determine new interest
    interest = mortgage_amount *(interest_rate/12)
    interest_paid_list.append(interest+interest_paid_list[month-1])
    #determine pricipal paid and remaining
    principal = payment - interest
    mortgage_amount -= principal
    mortgage_list.append(mortgage_amount)
    principal_paid_list.append(principal+principal_paid_list[month-1])


plot(month_list, mortgage_list, label="Remaining Mortgage", color = "red")
plot(month_list, principal_paid_list, label="Principal Paid", color = "blue")
plot(month_list, interest_paid_list, label="Interest Paid", color = "green")

axis([0,month,0,max(interest_paid_list[month], mortgage_list[0])])

legend()

show()


