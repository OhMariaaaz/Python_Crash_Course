# Exercise 6.5

languages = {
    'Russia': 'Russian',
    'Spain': 'Spanish',
    'Brazil': 'Portuguese',
    'England': 'English',
    'Germany': 'German'
}

for country, idiom in languages.items():
    print("In " + country + ", people speak " + idiom)

for country in languages.keys():
    print(country)

for idiom in languages.values():
    print(idiom)
