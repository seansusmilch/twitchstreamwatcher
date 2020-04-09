import os
from pathlib import Path

dir = str(Path(__file__).parent.absolute())

def setup():
    user = input("Twitch Username: ")
    passwd = input("Twitch Password: ")

    f = open(dir+'/secrets.py','w')
    f.write(
        "user = '" + user + "'\n"
        "passwd = '" + passwd + "'"
        )
    f.close

    print('setup done')

if not os.path.exists(dir+'/secrets.py'):
    setup()

from watchStream import watchSteam
watchSteam()
input('press enter to exit')