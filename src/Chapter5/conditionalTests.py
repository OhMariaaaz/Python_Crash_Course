# Exercise 5.1, 5.2

pokemon = 'Gengar'
type_pokemon = 'Ghost'

print("Is pokemon = 'Gengar'? I predict TRUE!")
print(pokemon == 'Gengar')

print("Is pokemon = 'Clefairy'? I predict FALSE!")
print(pokemon == 'Clefairy')

print("Is type_pokemon != 'Ghost' or pokemon != 'Gengar'? I predict FALSE!")
print(type_pokemon.lower() != 'Ghost' or pokemon.lower() != 'Gengar')

print("Is type_pokemon == 'Ghost' and pokemon == 'Gengar'? I predict FALSE(just because of the .lower() def rs)!")
print(type_pokemon.lower() == 'Ghost' and pokemon.lower() == 'Gengar')

print("Is type_pokemon == 'Ghost' or pokemon == 'Gengar'? I predict TRUE!")
print(type_pokemon == 'Ghost' or pokemon == 'Gengar')

print("Is type_pokemon == 'Fairy' and pokemon == 'Clefairy'? I predict FALSE!")
print(type_pokemon == 'Fairy' and pokemon == 'Clefairy')

pokemon = 'Clefairy'
type_pokemon = 'Fairy'

print("Is pokemon = 'Gengar'? I predict FALSE!")
print(pokemon == 'Gengar')

print("Is pokemon = 'Clefairy'? I predict TRUE!")
print(pokemon == 'Clefairy')

print("Is type_pokemon != 'Fairy' or pokemon != 'Clefairy'? I predict FALSE!")
print(type_pokemon != 'Fairy' or pokemon != 'Clefairy')

print("Is type_pokemon == 'Fairy' and pokemon == 'Clefairy'? I predict TRUE!")
print(type_pokemon == 'Fairy' and pokemon == 'Clefairy')

print("Is type_pokemon == 'Fairy' or pokemon == 'Clefairy'? I predict TRUE!")
print(type_pokemon == 'Fairy' or pokemon == 'Clefairy')

print("Is type_pokemon == 'Ghost' and pokemon == 'Gengar'? I predict FALSE!")
print(type_pokemon == 'Ghost' and pokemon == 'Gengar')

my_age = 21
husband_age = 25
middle_brother_age = 12
youngest_bother_age = 7

print("I'm older than my husband? I predict FALSE!")
print(my_age > husband_age)

print("I'm older(or have the same age) than my middle brother? I predict TRUE!")
print(my_age >= middle_brother_age)

print("I'm younger than my youngest brother? I predict FALSE!")
print(my_age < youngest_bother_age)

print("I'm younger(or have the same age) than my husband? I predict TRUE!")
print(my_age <= husband_age)

my_games = ['Dragon Age Inquisition','ESO Online','Borderlands']

print("Do I have Divinity 2 in my game storage? I predict FALSE!")
print('Divinity 2' in my_games)