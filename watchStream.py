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
        lowMin = 4
        hiMin = 60
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
    #go to drops enabled streams https://www.twitch.tv/directory/game/VALORANT?tl=c2542d6d-cd10-4532-919b-3d19f30a768b

    while True:
        print('Going to Valorant streams')
        driver.get('https://www.twitch.tv/directory/game/VALORANT?tl=c2542d6d-cd10-4532-919b-3d19f30a768b')
        time.sleep(2)
        
        elements = driver.find_elements_by_class_name('tw-link')
        elements[random.randint(0,len(elements))].click()
        time.sleep(1)

        # See if twitch went to the /videos section for some reason and go to the channels live stream if it did
        if '/videos' in driver.current_url:
            print('going to live')
            driver.get(driver.current_url.split('/videos')[0])
        time.sleep(1)

        # See if its an inappropriate stream and click Start Watching if it is
        elements = driver.find_elements_by_xpath('//*[text()="Start Watching"]')
        if len(elements) == 1:
            elements[0].click()

        print("Sleeping now (-.-) zzz")
        randSleep()
        print("Aight I'm out")