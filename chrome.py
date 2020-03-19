from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import base64, time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driverpath = './chromedriver'
driver = webdriver.Chrome(executable_path=driverpath, options=chrome_options)

driver.get("https://www.boce.com") #前往這個網址

url_input = driver.find_element_by_class_name('el-input__inner')
url_input.send_keys('www.tonnyshanghai.com')

url_enter = driver.find_elements_by_class_name('el-button--primary')[1]
url_enter.click()

while(True):
    try:
        result_button = driver.find_element_by_css_selector('.result-wrap .detail-wrap .el-button')
        result_button.click()
        break
    except:
        pass

map = driver.find_element_by_tag_name('canvas')
canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", map)
canvas_png = base64.b64decode(canvas_base64)

with open(r"canvas.png", 'wb') as f:
    f.write(canvas_png)

time.sleep(10)
driver.close()
