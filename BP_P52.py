# Python Program

# Create Class

class Employee():
    # Define Mehod

    # Initialize values
    # def __init__(self, name = chr, department = chr, salary = int):
    #     self.name = name
    #     self.department = department
    #     self.salary = salary
    
    def read(self):
        self.name = input("Enter Employee Name: ")
        self.department = input("Enter Department Name: ")
        self.salary = int(input("Enter Employee Salary: "))

    # Display Details
    def output(self):
        print("**************** Employee Details ****************")
        print("Employee Name: ", self.name)
        print("Employee Department: ", self.department)
        print("Employee Salary: ", self.salary ," RS")

# Create class object
emp = Employee()

# Call Method
# emp.__init__("Rahul", "Software Developer", 50000)

# Read values Method
emp.read()

# show details Method
emp.output()

# Thanks for Watching
    

        