# Let's review class methods
class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return('{}, {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    # class methods are created using @classmethod
    @classmethod    # NOTE this alters the functionality of our method so that now we recieve the class as our first argument instead of the instance
    # NOTE cls is the convention to refer to the class. the is the same exact thing as self referring to the instance. cls intead of class since that's a keyword in python.
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


emp_1 = Employee('Aaron', 'Glenn', 100)
emp_2 = Employee('Test', 'User', 200)

# NOTE that the cls argument of our set_raise_amt method is added automatically.
Employee.set_raise_amt(1.5)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Class methods as alternative constructors. What does this mean? you can use these class methods in order to provide multiple wasy of creating our objects.

# in this case, someone is trying to parse out a string of an employee's name from the given string.

emp_str_1 = 'Aaron-Glenn-101'
emp_str_1 = 'Edward-Glenn-201'
emp_str_1 = 'Aaron-Edward-301'

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
