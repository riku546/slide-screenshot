from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By




def slide_count(page_url):
    options = Options()

    #以下の二つの引数を変更する
    options.add_argument("--user-data-dir=C")
    options.add_argument('--profile-directory=')

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
