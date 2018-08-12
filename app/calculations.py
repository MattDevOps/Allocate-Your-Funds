import locale
locale.setlocale( locale.LC_ALL, '' ) # sets salary to USD

class Calculations():
    def __init__(self, age, salary, risk):
        self.age = age
        self.salary = float(salary)
        self.risk = risk

    #method is called if user is risky
    def stocks_yes(self):
        user_stock = (120 - self.age)
        return user_stock

    #method is called if user is risk averse
    def stocks_no(self):
        user_stock = (90 - self.age)
        return user_stock

    #calculates how much $ the user should hold
    def five_percent(self):
        user_salary = (self.salary * 0.05)
        return locale.currency(user_salary, grouping=True)

    #displayed in table header
    def get_age(self):
        return self.age

    #displayed in table header
    def get_salary(self):
        return locale.currency(self.salary, grouping=True)

    #displayed in table header
    def is_risky(self):
        return self.risk

    #determines how much we recommend the user invest in stocks
    def get_risk(self):
        if self.risk == 'yes' or 'Yes':
            return self.stocks_yes()
        elif self.risk == 'no' or 'No':
            return self.stocks_no()
