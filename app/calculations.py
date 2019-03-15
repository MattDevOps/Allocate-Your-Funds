import locale
locale.setlocale( locale.LC_ALL, '' ) # sets salary to USD

class Calculations():
    def __init__(self, age, salary, risk):
        self.age = age
        self.salary = float(salary)
        self.risk = risk

    # one of these methods will get called depending on user's risk level
    def stocks_5(self):
        user_stock = (100 - self.age)
        return int(user_stock)

    def stocks_4(self):
        user_stock = (90 - self.age)
        return int(user_stock)

    def stocks_3(self):
        user_stock = (80 - self.age)
        return int(user_stock)

    def stocks_2(self):
        user_stock = (70 - self.age)
        return int(user_stock)

    def stocks_1(self):
        user_stock = (60 - self.age)
        return int(user_stock)

    def one_percent(self):
        user_salary = (self.salary * 0.01)
        return locale.currency(user_salary, grouping=True)

    def two_percent(self):
        user_salary = (self.salary * 0.02)
        return locale.currency(user_salary, grouping=True)

    #calculates % of the user's salary, returns value in cash to hold
    def three_percent(self):
        user_salary = (self.salary * 0.03)
        return locale.currency(user_salary, grouping=True)

    def four_percent(self):
        user_salary = (self.salary * 0.04)
        return locale.currency(user_salary, grouping=True)

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

    #determines how much we recommend for the user to invest in stocks
    def get_risk(self):
        print(self.risk)
        if int(self.risk) == 1:
            return self.stocks_1()
        elif int(self.risk) == 2:
            return self.stocks_2()
        elif int(self.risk) == 3:
            return self.stocks_3()
        elif int(self.risk) == 4:
            return self.stocks_4()
        elif int(self.risk) == 5:
            return self.stocks_5()

    #displayed on results page - how much cash the user should hold, based on their risk level
    def get_percent(self):
        if int(self.risk) == 1:
            return self.one_percent()
        elif int(self.risk) == 2:
            return self.two_percent()
        elif int(self.risk) == 3:
            return self.three_percent()
        elif int(self.risk) == 4:
            return self.four_percent()
        elif int(self.risk) == 5:
            return self.five_percent()
