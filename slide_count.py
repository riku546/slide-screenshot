from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By




def slide_count(page_url):
    options = Options()
# page_url = "https://docs.google.com/presentation/d/e/2PACX-1vRaMwHlOn6-5FvAyqi6puXfEoN8xxzxhfUErJ0WSV85iWoSaJqHqmXlZeYGA0_stg/embed?start=false&loop=false&delayms=3000&slide=id"
# page_url2 = "https://docs.google.com/presentation/d/e/2PACX-1vQG0Yhr0DnC74095EIDQWIhi8AXSVzlwp4nB-DDn89bD585IcN12-dC5x94k9DDzQ/embed?start=false&loop=false&delayms=3000&slide=id"
# page_url3 = "https://docs.google.com/presentation/d/e/2PACX-1vQN3CLyNuuYg2B6jT0mZR14sP4zyw3iMkEebNkSB3toTJ1UgT9qAhf6C777hhJ0-A/embed?start=false&loop=false&delayms=3000&slide=id"
# page_url4 = "https://docs.google.com/presentation/d/e/2PACX-1vSH_eiyPclqpWx-UYKz-kHmOJwHOoggiS5sgGxraVxiXBdfT2u19SWPY3D_4TZSag/embed?start=false&loop=false&delayms=60000&slide=id"
    #以下の二つの引数を変更する
    options.add_argument("--user-data-dir=C:/Users/opa97/AppData/Local/Google/Chrome/User Data/")
    options.add_argument('--profile-directory=Profile 2')

    driver = webdriver.Chrome(options=options)

    url = f"{page_url}.p1"
    driver.get(url)

    docs_ui_unprintable = driver.find_element(By.CLASS_NAME , "docs-ui-unprintable")




    punch_viewer_navbar = docs_ui_unprintable.find_element(By.CLASS_NAME , "punch-viewer-navbar")



    div = punch_viewer_navbar.find_element(By.TAG_NAME , "div")




    div2 = div.find_element(By.CLASS_NAME , "punch-viewer-navbar-page")




    slide_num_div = div2.find_element(By.CLASS_NAME , "goog-inline-block")




    slide_num = slide_num_div.get_attribute("aria-setsize")

    driver.quit()

    
    return slide_num
