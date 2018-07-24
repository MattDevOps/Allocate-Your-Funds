from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(256))
    age = db.Column(db.Integer)
    salary = db.Column(db.Integer)

    def bonds(self, age, salary):
        pass

    def hold_cash(self, age, salary):
        pass

    def stocks(self, age, salary):
        pass

    def five_percent(self, salary):
        return (salary * 0.05)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'Username = {}, Email = {}, Age={}, Salary={}'.format(self.username, self.email, self.age, self.salary)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
