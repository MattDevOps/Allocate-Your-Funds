class Calculations():
    def __init__(self, age, salary):
        self.age = age
        self.salary = salary

    def stocks(self):
        user_stock = (118 - self.age)
        return int(user_stock)

    def holdCash(self):
        return 'This is a string, going to the results.html file'

    def bonds(self):
        pass

    def five_percent(self):
        user_salary = (self.salary * 0.05)
        return int(user_salary)

    def get_age(self):
        user_age = (0 + self.age)
        return int(user_age)

    def get_salary(self):
        user_salary = (0 + self.salary)
        return int(user_salary)
