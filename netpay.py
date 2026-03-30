#caluculating the net pay
#gross pay =(Gross pay * tax rate)
def salary():
    gross = 2500000
    return gross

#calculating tax

def tax():
    return salary() * 0.3

tax()
print(tax())

#calculating NSSF
def nssf():
    return salary() * 0.05
nssf()
print(nssf())

# calculating other deductions
def other_deductions():
    return salary() * 0.05

other_deductions()
other_deductions()
print(other_deductions())

#calculating the total
def total_taxes():
    return (tax() + nssf() + other_deductions())
total_taxes()
print("total tax is: ", total_taxes())

# Am calculating the netpay(grosspay-total_tax)
def net_pay():
    return salary() - total_taxes()
    return net_pay
net_pay()
print("total net pay is: ", net_pay())

  
