class Calculations():
    def __init__(self, age, salary, risk):
        self.age = age
        self.salary = float(salary)
        self.risk = risk

    #method is called if user is risky
    def stocks_yes(self):
        user_stock = (120 - self.age)
        str_user_stock = str(user_stock)
        if len(str_user_stock) == 4:
            return '${:4,.2f}'.format(user_stock)
        elif len(str_user_stock) == 5:
            return '${:5,.2f}'.format(user_stock)
        elif len(str_user_stock) == 6:
            return '${:6,.2f}'.format(user_stock)
        elif len(str_user_stock) == 7:
            return '${:7,.2f}'.format(user_stock)
        elif len(str_user_stock) == 8:
            return '${:8,.2f}'.format(user_stock)
        elif len(str_user_stock) == 9:
            return '${:9,.2f}'.format(user_stock)
        else:
            return '$' + '' + str(user_stock)

    #method is called if user is risk averse
    def stocks_no(self):
        user_stock = (98 - self.age)
        str_user_stock = str(user_stock)
        if len(str_user_stock) == 4:
            return '${:4,.2f}'.format(user_stock)
        elif len(str_user_stock) == 5:
            return '${:5,.2f}'.format(user_stock)
        elif len(str_user_stock) == 6:
            return '${:6,.2f}'.format(user_stock)
        elif len(str_user_stock) == 7:
            return '${:7,.2f}'.format(user_stock)
        elif len(str_user_stock) == 8:
            return '${:8,.2f}'.format(user_stock)
        elif len(str_user_stock) == 9:
            return '${:9,.2f}'.format(user_stock)
        else:
            return '$' + ' ' + user_stock

    def bonds(self):
        pass

    #calculates how much $ the user should hold
    def five_percent(self):
        user_salary = (self.salary * 0.05)
        str_user_salary = str(user_salary)
        if len(str_user_salary) == 4:
            return '${:4,.2f}'.format(user_salary)
        elif len(str_user_salary) == 5:
            return '${:5,.2f}'.format(user_salary)
        elif len(str_user_salary) == 6:
            return '${:6,.2f}'.format(user_salary)
        elif len(str_user_salary) == 7:
            return '${:7,.2f}'.format(user_salary)
        elif len(str_user_salary) == 8:
            return '${:8,.2f}'.format(user_salary)
        elif len(str_user_salary) == 9:
            return '${:9,.2f}'.format(user_salary)
        else:
            return '$' + '' + str(user_salary)

    def get_age(self):
        return self.age

    def get_salary(self):
        str_salary = str(self.salary)
        if len(str_salary) == 4:
            return '${:4,.2f}'.format(self.salary)
        elif len(str_salary) == 5:
            return '${:5,.2f}'.format(self.salary)
        elif len(str_salary) == 6:
            return '${:6,.2f}'.format(self.salary)
        elif len(str_salary) == 7:
            return '${:7,.2f}'.format(self.salary)
        elif len(str_salary) == 8:
            return '${:8,.2f}'.format(self.salary)
        elif len(str_salary) == 9:
            return '${:9,.2f}'.format(self.salary)
        else:
            return '$' + ' ' + self.salary

    #used for table header
    def is_risky(self):
        return self.risk

    def get_risk(self):
        if self.age == 'yes' or 'Yes':
            return Calculations.stocks_yes(self)
        else:
            return Calculations.stocks_no(self)
