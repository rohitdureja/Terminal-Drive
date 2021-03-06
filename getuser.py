import json
from time import strftime
from getcredentials import get_credential_file, get_credentials

# reads JSON file and checks if user already exists
def check_if_user_exists(email):
    # Open the user list JSON file for reading
    with open('json/users.json', 'r') as user_file:
        # Read users 
        users = json.load(user_file)
    # Check if user exists
    # If user exists, update the login time
    if email in users:
        print "Last login: " + users[email]['last-login']
        # Open file for writing
        with open('json/users.json', 'w') as user_file:
            # Update users in JSON
            users[email]['last-login'] = strftime("%Y-%m-%d %H:%M:%S")
            # Update JSON file with updated data
            json.dump(users, user_file, indent=4)
        
        return users[email]
    else:
        return False

# creates new user and updates the JSON file
def create_new_user(email):
    # Create JSON entry for new user
    entry = {email : {'credential': 'Undefined', 'directory-tree' : 'Undefined', 'last-login': strftime("%Y-%m-%d %H:%M:%S")}}

    # Open file for reading
    with open('json/users.json', 'r') as user_file:
        users = json.load(user_file)
    
    # Open file for writing
    with open('json/users.json', 'w') as user_file:
        # Update users in JSON
        users.update(entry)
        # Update JSON file with updated data
        json.dump(users, user_file, indent=4)
    
    return users[email]

# get user data from JSON file
def get_user_data(email):
    # Open the user list JSON file for reading
    with open('json/users.json', 'r') as user_file:
        # Read users 
        users = json.load(user_file)
    # return user data
    return users[email]

# update user credentials in file
def update_credential_in_file(email, credential):
    # Open file for reading
    with open('json/users.json', 'r') as user_file:
        users = json.load(user_file)
    
    # Open file for writing
    with open('json/users.json', 'w') as user_file:
        # Update users in JSON
        users[email]['credential'] = credential
        # Update JSON file with updated data
        json.dump(users, user_file, indent=4)


def get_user(email):
    user = check_if_user_exists(email)
    if not user:
        print "User doesn't exist. Adding new user ..."
        user = create_new_user(email)
        credential_file = get_credential_file(email)
        update_credential_in_file(email, credential_file)
        user = get_user_data(email)
    
    return get_credentials(user['credential'])
        
        