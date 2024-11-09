# Exercises 6.1, 6.2, 6.7, 6.8, 6.11 and 6.12

party_characters = {
    'Rodrigo':['Enarius','RosGalthar'],
    'Goes': ['GM','Hofio'],
    'Kaio': ['Vermax','Tam'],
    'Luiz': ['Vermut','Santo Ernesto']
    }

for character in party_characters.items():
    print(character)

character_1 = {
    'name':"Geslav",
    'race':"Elven",
    'age':548
    }

character_2 =  {
    'name':"Mikha",
    'race':"Goblin",
    'age':3
    }

character_3 =  {
    'name':"CiCi Furacão",
    'race':"Ratfolk",
    'age': 18
    }


my_characters = (character_1, character_2, character_3)
'''
for character in my_characters:
    print(character)
'''


guild_rpg = {
'kralk_lycan_hell': {'race':'drakob','total_xp':1205},
'dashka_dessari': {'race':'zahir','total_xp':1405},
'kahlisah_lozzern': {'race':'soole','total_xp': 550},
'kralk_lycan_hell': {'race':'drakob','total_xp':1205},
'john_silva': {'race':'human','total_xp':2035},
'hiashi_cabecao': {'race':'iskoro','total_xp':1000}
            }

'''
for character, character_info in guild_rpg.items():
    print(character + "\n" + str(character_info) + "\n")
'''

