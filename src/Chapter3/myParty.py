# Exercises 3.4, 3.5, 3.6, 3.7 and 3.9
party_friends = ["Ros'Galthar","TT","Hofio","Santo Ernesto","Percival","Geslav","L30"]
print(party_friends[6] + "was removed from the server.")
party_friends[6] = "Mikha"

for i in party_friends:
    print(i + "! Welcome to the server!")

print("Now we have a bigger session! I convited more characters to join or campaign.")
new_members = ["Dra. Choo","Glitch","Avi","Whisky"]
party_friends.insert(0,new_members[0])
party_friends.insert(2,new_members[1])
party_friends.append(new_members[2])
party_friends.append(new_members[3])

for i in party_friends:
    print(i + "! Welcome to the server!")

print(len(party_friends))

while len(party_friends) >= 3:
    popped = party_friends.pop()
    print(popped + ", I'm so sorry... But your character died. Good bye and good luck!")

for i in party_friends:
    print(i + " has achieved a new level!")

del party_friends[0]
del party_friends[0]

print(party_friends)