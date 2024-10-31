# Exercises 6.3 and 6.4

new_words = {
    'API':'The API is responsable to made connectin between system and user.',
    'DevOps': 'Culture and methods that conect operational and development processes,'
    'focused on productive results and security.',
    'Featured Flags': 'A tool to do tests and updates in real time, and using real persons',
    'Dictionary': 'Key-Value style list.',
    'List': 'An ordened list of variables.',
    'Variable': 'Variable is a space reserved to hold data for a short time.',
    'Indentation': 'Organization of code using spaces to create a visual hierarquic of elements and codes.',
    'Data Type': 'The type of data is what define how data will be collect and storage: int, double, string, etc.',
    'Function': 'A piece of code that you can call multiples times in the aplication.',
    'AI': 'Artificial Inteligence.',
    }

for word, meaning in new_words.items():
    print(word + "\n" + meaning + "\n")
