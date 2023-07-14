import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# var for chrome driver
chrome_driver_path = 'C:\\Users\\eshin\\Desktop\\chromedriver.exe'

chrome_profile_path = 'C:\\Users\\eshin\\AppData\\Local\\Google\\Chrome\\User Data\\Default'

# url var
website_url = 'https://foreupsoftware.com/index.php/booking/19765/2431#teetimes'

# first btn var
button_text = 'Resident'

# rsv date
date_to_click = 14

# rsv time
time_label_to_click = '12:10pm'

chrome_options = Options()
chrome_options.add_argument(f'--user-data-dir={chrome_profile_path}')
chrome_options.add_argument("--start-maximized")

# service start var
service = Service(chrome_driver_path)

# driver start var
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    target_time = datetime.now().replace(hour=1, minute=33, second=58, microsecond=0)
    
    while datetime.now() < target_time:
        time.sleep(1)
        
    # open site
    driver.get(website_url)

    # click first btn 'resident'
    resident_button = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, f'//button[@class="btn btn-primary col-md-4 col-xs-12 col-md-offset-4"][text()="{button_text}"]'))
    )
    resident_button.click()

    time.sleep(2)

    # var -> date click
    date_element = driver.find_element(By.XPATH, f'//td[@class="day" and text()="{date_to_click}"]')
    date_element.click()

    # Wait for a few seconds to see the result
    time.sleep(2)

    # var -> time click
    time_label_element = driver.find_element(By.XPATH, f'//div[@class="booking-start-time-label" and text()="{time_label_to_click}"]')
    time_label_element.click()

    # number of players
    number_element = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="btn btn-primary " and @data-value="4"]')))
    number_element.click()

    # booko rsv
    book_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-success js-book-button pull-left"]')))
    book_button.click()
  
    time.sleep(10)

finally:
    # Close the WebDriver session
    driver.quit()
 
