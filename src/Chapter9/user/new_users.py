# Exercise 9.3

from user import User

users = {}
users['OhMariaaz'] = User("OhMariaaz", "maria", "gomes", "Brazil", "A software developer" +
                          " with a passion for video games. In his free time, he streams" +
                          " his gaming sessions online")
users['WanderlustSarah'] = User("WanderlustSarah", "Sarah", "Montgomery", "United States", 
                                "I can speak three languages fluently: English, Spanish, " +
                                "and French.")
users['MeiStyle'] = User("MeiStyle", "Mei", "Tanaka", "Japan", "Mei is a fashion designer" +
                         " who blends traditional Japanese fabrics with modern styles. ")
users['LiamTheChef'] = User("LiamTheChef", "Liam", "O'Connor", "Ireland", "Liam is a " +
                            "professional chef who specializes in sustainable cooking")

for user in users.values():
    user.describe_user()
    user.greet_user()

'''
users['LiamTheChef'].increment_login_attempts()
users['LiamTheChef'].increment_login_attempts()
users['LiamTheChef'].increment_login_attempts()
users['MeiStyle'].increment_login_attempts()
users['MeiStyle'].increment_login_attempts()
users['MeiStyle'].increment_login_attempts()
users['WanderlustSarah'].increment_login_attempts()
users['WanderlustSarah'].increment_login_attempts()
users['OhMariaaz'].increment_login_attempts()
users['MeiStyle'].increment_login_attempts()
users['WanderlustSarah'].increment_login_attempts()
users['OhMariaaz'].increment_login_attempts()
users['MeiStyle'].increment_login_attempts()
users['WanderlustSarah'].increment_login_attempts()
users['LiamTheChef'].increment_login_attempts()
users['LiamTheChef'].increment_login_attempts()
users['WanderlustSarah'].increment_login_attempts()
users['LiamTheChef'].increment_login_attempts()
users['LiamTheChef'].increment_login_attempts()
users['LiamTheChef'].increment_login_attempts()
users['MeiStyle'].increment_login_attempts()
users['WanderlustSarah'].increment_login_attempts()
users['LiamTheChef'].increment_login_attempts()
users['LiamTheChef'].increment_login_attempts()
users['MeiStyle'].increment_login_attempts()
users['WanderlustSarah'].increment_login_attempts()
users['OhMariaaz'].increment_login_attempts()
users['MeiStyle'].increment_login_attempts()
users['WanderlustSarah'].increment_login_attempts()
users['LiamTheChef'].increment_login_attempts()
users['MeiStyle'].increment_login_attempts()
users['WanderlustSarah'].increment_login_attempts()
users['LiamTheChef'].increment_login_attempts()
users['LiamTheChef'].increment_login_attempts()


for user in users.values():
    user.describe_user()
    user.greet_user()

for user in users.values():
    user.reset_login_attempts()

for user in users.values():
    user.describe_user()
    user.greet_user()
'''
