import time
from datetime import datetime
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

# url var
website_url = 'https://foreupsoftware.com/index.php/booking/19765/2431#teetimes'

# first btn var
button_text = 'Resident'

# rsv date
date_to_click = 23

# rsv time
time_label_to_click = '12:00pm'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:5556")  # Use your existing Chrome debugging address

# driver start var
driver = webdriver.Chrome(options=chrome_options)

try:
    target_time = datetime.now().replace(hour=18, minute=59, second=58, microsecond=30)

    while datetime.now() < target_time:
        time.sleep(1)

    # open site
    driver.get(website_url)

    # click first btn 'resident'
    resident_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, f'//button[@class="btn btn-primary col-md-4 col-xs-12 col-md-offset-4"][text()="{button_text}"]'))
    )
    resident_button.click()

    select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'schedule_select'))
    )

    # select var
    select = Select(select_element)

    # drop down select
    select.select_by_value('2432')

    # Re-locate the select element after selecting the option
    select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'schedule_select'))
    )

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
