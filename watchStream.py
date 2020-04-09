import random
import time
from datetime import datetime
from os import path
from secrets import passwd, user

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from drive import driverWithDelay


def watchSteam():
    dir = path.split(path.abspath(__file__))
    dir = dir[0]

    def randSleep():
        lowMin = 2
        hiMin = 36
        slp = random.randint(lowMin,hiMin) * (random.randint(70,101) / (100 + random.randint(0,10)))
        print(datetime.now().strftime("%H:%M"),' - sleeping for ',slp,' minutes')
        time.sleep(slp * 60)

    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.add_argument("--mute-audio")
    driver = webdriver.Chrome(options=chromeoptions,executable_path= dir + "/chromedriver.exe")

    driver.get('https://twitch.tv/login')
    drive = driverWithDelay(driver, 1)

    drive.send('/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[1]/div/div[2]/input',user)
    drive.send('/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[2]/div/div[1]/div[2]/div[1]/input',passwd)
    drive.click('/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/button')

    timeout = 30
    while driver.title == 'Log In - Twitch' and timeout > 0:
        print('Please type in authentication ' + str(timeout))
        time.sleep(1)
        timeout -= 1
        
    print('Logged in!')
    time.sleep(2)
    #go to https://www.twitch.tv/directory/game/VALORANT

    while True:
        print('Going to Valorant streams')
        driver.get('https://www.twitch.tv/directory/game/VALORANT')
        time.sleep(2)
        drive.click('//*[@id="root"]/div/div[2]/div/main/div[1]/div[3]/div/div/div/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]/div/div/div/div/article/div[1]/div/div[1]/div[3]/div/div/div[2]/button')

        #click a random stream and sit there for a lil bit

        elements = driver.find_elements_by_class_name('tw-link')
        elements[random.randint(0,100)].click()
        print("Sleeping now (-.-) zzz")
        randSleep()
        print("Damn this shit boring")
