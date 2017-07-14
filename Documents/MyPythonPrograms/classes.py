# class Employee:
#    #Common base class for all employees'
#    empCount = 0

#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
   
#    def displayCount(self):
#      print "Total Employee %d" % Employee.empCount

#    def displayEmployee(self):
#       print "Name : ", self.name,  ", Salary: ", self.salary

# #This would create first object of Employee class
# emp1 = Employee("Paa Kwesi", 2000)
# #This  would create first object of Employee class
# emp2 = Employee("Blankson", 9000)

# #Accessing Attributes 
# emp1.displayEmployee()
# emp2.displayEmployee()
# print "Total Employee %d" % Employee.empCount 


#Adding total salary to the class
class Employee:
   #Common base class for all employees'
   empCount = 0
   totalSalary = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
      Employee.totalSalary += salary
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

# #This would create first object of Employee class
emp1 = Employee("Paa Kwesi", 2000)
# #This  would create first object of Employee class
# emp2 = Employee("Blankson", 9000)

# #Accessing Attributes 
# emp1.displayEmployee()
# emp2.displayEmployee()
# print "Total Employee %d" % Employee.empCount
# print "Total Salary paid %d" % Employee.totalSalary 

emp1.age = 7
emp1.age = 8
print emp1.age   


print hasattr(emp1, "age") #Returns true if age attribute exist
print getattr(emp1, "age") #Returns value of age attribute 

# setattr(emp1, 'age', 8) # Set attribute 'age' at 8
# delattr(empl, 'age')    # Delete attribute 'age'
