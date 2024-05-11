import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from slide_count import slide_count
from setting import Profile_location , Profile_name


def screen_shot ( page_url , dir_name):

    os.mkdir(dir_name)
    slide_num = int(slide_count(page_url))

    options = Options()

    options.add_argument(f"--user-data-dir={Profile_location}")
    options.add_argument(f'--profile-directory={Profile_name}')

    driver = webdriver.Chrome(options=options)
 


    
    for i in range(slide_num):

        url = f"{page_url}.p{i + 1}"
        driver.get(url)
        driver.save_screenshot(f"{dir_name}\screen{i + 1}.jpg")
    
    driver.quit()
    # https://docs.google.com/presentation/d/e/2PACX-1vRaMwHlOn6-5FvAyqi6puXfEoN8xxzxhfUErJ0WSV85iWoSaJqHqmXlZeYGA0_stg/embed?start=false&loop=false&delayms=3000&slide=id


page_url = input("ページのURLをにゅうりょくしてください:")
dir_name = input("作成するフォルダー名を入力していください:")
screen_shot( page_url, dir_name)
