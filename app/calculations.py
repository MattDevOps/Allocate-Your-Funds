class Calculations():
    def __init__(self, age, salary, risk):
        self.age = age
        self.salary = salary
        self.risk = risk

    def stocks_yes(self):
        user_stock = (118 - self.age)
        return int(user_stock)

    def stocks_no(self):
        user_stock = (98 - self.age)
        return int(user_stock)

    def bonds(self):
        pass

    def five_percent(self):
        user_salary = (self.salary * 0.05)
        return int(user_salary)

    def get_age(self):
        return self.age

    def get_salary(self):
        return self.salary

    def get_risk(self):
        if self.age == 'yes' or 'Yes':
            return Calculations.stocks_yes(self)
        else:
            return Calculations.stocks_no(self)
