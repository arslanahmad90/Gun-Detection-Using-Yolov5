with open('datasheet.txt') as f:
    data = f.read()
    credentials = eval(data)
    usernames = list(credentials.keys())
    passwords = list(credentials.values())
print(usernames)
print(passwords)