from os import path

user = input("Twitch Username: ")
passwd = input("Twitch Password: ")

f = open('secrets.py','w')
f.write(
    "user = '" + user + "'\n"
    "passwd = '" + passwd + "'"
    )
f.close

print('done!')