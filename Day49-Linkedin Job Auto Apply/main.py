from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


MY_EMAIL = "***************"
MY_PASSWORD = "*********"
PHONE = "*******"

chrome_driver_path = "/Users/queenasong/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2%2C3&geoId=102095887&keywords=financial%20analyst&location=California%2C%20United%20States&sortBy=R")
driver.maximize_window()


time.sleep(2)
sign_in_bar = driver.find_element_by_link_text("Sign in")
sign_in_bar.click()

time.sleep(3)
username = driver.find_element_by_name("session_key")
username.send_keys(MY_EMAIL)

password = driver.find_element_by_name("session_password")
password.send_keys(MY_PASSWORD)
# password.send_keys(Keys.ENTER)

sign_in_button = driver.find_element_by_css_selector(".btn__primary--large")
sign_in_button.click()

time.sleep(5)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")
print(all_listings)

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        dismiss_button = driver.find_element_by_css_selector(".artdeco-toast-item__dismiss")
        dismiss_button.click()
        time.sleep(1)
    except Exception as err:
        print(f"{err}: Continuing")
        continue


        #Locate the apply button
    try:
        time.sleep(1)
        apply_button = driver.find_element_by_css_selector(".jobs-apply-button")
        apply_button.click()
        time.sleep(1)

        #If phone field is empty, then fill your phone number.
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element_by_css_selector(".artdeco-modal__actionbar .artdeco-button--primary")
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue



time.sleep(5)
driver.quit()