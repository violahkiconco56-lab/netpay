#how  functions communicate
# funtions communicate 
def salary():
    gross = 2500000
    return gross
    stuff = 500000 

def tax():
    return salary() * 0.3

print(tax())
def expense():
    print(salary() - tax())

expense()