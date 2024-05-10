import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def screen_shot (n , page_url , dir_name):
    count = 0

    os.mkdir(dir_name)

    options = Options()
    #以下の２行で初期設定する
    options.add_argument("--user-data-dir=")
    options.add_argument('--profile-directory=')

    driver = webdriver.Chrome(options=options)
 


    
    for i in range(n):
        print(i)

        url = f"{page_url}.p{i + 1}"
        driver.get(url)
        driver.save_screenshot(f"{dir_name}\screen{i + 1}.jpg")
    
    driver.quit()
    # https://docs.google.com/presentation/d/e/2PACX-1vRaMwHlOn6-5FvAyqi6puXfEoN8xxzxhfUErJ0WSV85iWoSaJqHqmXlZeYGA0_stg/embed?start=false&loop=false&delayms=3000&slide=id


n =int(input("ページ数をにゅうりょくしてください："))
page_url = input("ページのURLをにゅうりょくしてください:")
dir_name = input("作成するフォルダー名を入力していください:")
screen_shot(n , page_url, dir_name)
