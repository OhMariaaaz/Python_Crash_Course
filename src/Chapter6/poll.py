# Exercise 6.6

favorite_languages = {
    'edward': 'ruby',
    'sarah': 'c',
    'phil': 'python',
    'jen': 'python'
}

poll_friends = ['edward', 'sarah', 'maria', 'phil', 'jen', 'erin']

for friend in poll_friends:
    if friend not in favorite_languages.keys():
      print("Hey, " + friend.title() + " what are you waiting for? Send your answer to our poll!!!")
    else:
        print("Thanks for helping our poll, " + friend.title() + "!") 
