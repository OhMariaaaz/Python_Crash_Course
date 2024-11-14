# Exercises 8.13 and 8.17

def build_profile(first_name, last_name, **user_info):
    '''Register information from new users'''
    new_user = {}
    new_user['First'] = first_name
    new_user['Last'] = last_name
    for key, info in user_info.items():
        new_user[key] = info

    return new_user


user_one = build_profile('Maria', 'Gomes', country='Brazil', age=21, 
                         birthday='24/04/2003')

print(user_one)

