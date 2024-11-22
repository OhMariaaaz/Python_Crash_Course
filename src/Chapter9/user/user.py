# Exercise 9.3

class User():

    def __init__(self, username, first_name, last_name, country, about_me):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.about_me = about_me
        self.login_attempts = 0


    def describe_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title() + ". Your register is " + self.username)
        print("you're from " + self.country + "/n and here a little more about you: " + self.about_me)
    

    def greet_user(self):
        print("You have attemptd your login " + str(self.login_attempts) + " times.")
        print("Welcome, " + self.username + ". We have news for u today! \n")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):

    def __init__(self, username, first_name, last_name, country, about_me, *privilegies):
        super().__init__(username, first_name, last_name, country, about_me)
        self.privilegies = privilegies

    def show_privilegies():


