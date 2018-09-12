class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        
# Inheritance
# Every City is a kind of Location

class City(Location):
    def __init__(self, name, county, state, population, latitude, longitude):
        Location.__init__(self, latitude, longitude)
        self.name = name;
        self.county = county;
        self.state = state;
        self.population = population;

# class City(Location):
#     def __init__(self, name, county, state, population, latitude, longitude):
#         super(self, Location).__init__(self, latitude, longitude)
#         self.name = name;
#         self.county = county;
#         self.state = state;
#         self.population = population;
    
SF = City("SF", "SF", "CA", 7000000, 0, 1);

print(SF.name == "SF")
print(SF.county == "SF")
print(SF.state == "CA")
print(SF.population == 7000000)
print(SF.latitude == 0)
print(SF.longitude == 1)

'''
class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last) # this is like calling super of the parent
        self.staffnumber = staffnum

    def GetEmployee(self): # adding additional functionality -- extending the Person class
        return self.Name() + ", " +  self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.Name())
print(y.GetEmployee())
'''