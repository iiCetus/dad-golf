import time
from datetime import datetime
from selenium.webdriver.support.ui import Select
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
date_to_click = 21

# rsv time
time_label_to_click = '122:20pm'

chrome_options = Options()
chrome_options.add_argument(f'--user-data-dir={chrome_profile_path}')
chrome_options.add_argument("--start-maximized")

# service start var
service = Service(chrome_driver_path)

# driver start var
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    target_time = datetime.now().replace(hour=19, minute=50, second=0, microsecond=0)
    
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

    # drop down element
    select_element = driver.find_element(By.ID, 'schedule_select')

    # select var
    select = Select(select_element)

    # drop down select
    select.select_by_value('2432')

    # Re-locate the select element after selecting the option
    select_element = driver.find_element(By.ID, 'schedule_select')

    # Create a new Select object with the updated reference
    select = Select(select_element)

    # Click on the selected option
    selected_option = select.first_selected_option
    selected_option.click()

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
