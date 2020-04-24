# Class methods as alternative constructors. What does this mean? you can use these class methods in order to provide multiple wasy of creating our objects.
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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_1 = Employee('Aaron', 'Glenn', 100)
emp_2 = Employee('Test', 'User', 200)


emp_str_1 = 'Aaron-Glenn-101'
emp_str_2 = 'Edward-Glenn-201'
emp_str_3 = 'Aaron-Edward-301'


new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

# this is what it means to use class methods as constructors. we are constructing a new employee based on a method that takes a string, breaks it up, and sets the new employee based on the info we have taken.
