#offer calculator functions
def menu():
    print "Welcome to PdCalculator.py"
    print "your options are:"
    print " "
    print "1) Add"
    print "2) Subtract"
    print "3) Multiply"
    print "4) Divide"
    print "5) Quit PdCalculator.py"
    print " "
    return raw_input ("Choose your option: ")

#function for calculations
def add(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError
            
            
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        add(input("Add this: "),input("to this: "))
    elif choice == 2:
        sub(input("Subtract this: "),input("from this: "))
    elif choice == 3:
        mul(input("Multiply this: "),input("by this: "))
    elif choice == 4:
        div(input("Divide this: "),input("by this: "))
    elif choice == 5:
        loop = 0

print "Thankyou for using calculator.py!"
