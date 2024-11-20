# Exercise 9.3

from user import *

users = []
users.append(User("OhMariaaz", "maria", "gomes", "Brazil", "Today I'm starting my College of Information Systems."))

for user in users:
    user.describe_user()
    user.open_user()

