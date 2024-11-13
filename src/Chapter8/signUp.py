
def build_profile(first_name, last_name, **user_info):
    new_user = {}
    new_user['First'] = first_name
    new_user['Last'] = last_name
    for key, info in user_info.items():
        new_user[key] = info

    return new_user


user_one = build_profile('Maria', 'Goes', country='Brazil', age=21)

print(user_one)

