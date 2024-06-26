# Exercises 5.8, 5.9 and 5.10
current_users = ["TheGoes","Trevosinha","TheMary","Admin","BulletDancer","DarkHofio"]
new_users = ["darkHOFIO","Hosghaltar","Mashista","NotMyProblem","TRevOSinHA"]

for new_user in new_users:
    unique_name = True
    for current_user in current_users:
        if (new_user.lower() == current_user.lower()):
            print("This name is invalid, " + new_user + "!")
            unique_name = False
    if(unique_name == True):
        print("Welcome to our server " + new_user)
        current_users.append(new_user)

if current_users:
    for user in current_users:
        if user.lower() == "Admin".lower():
            print("Welcome, adm! Do you want to see some statics today?")
        else:
            print("Welcome " + user + "! Take a seat. The game will begin soon...")
else:
    print("We need to find more users!!!")