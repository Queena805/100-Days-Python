from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/queenasong/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")



# article_number = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# # article_number.click()
#
# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()
#
# search = driver.find_element_by_name("search")
# # search.send_keys("Python")
# # search.send_keys(Keys.ENTER)


first_name = driver.find_element_by_name("fName")
first_name.send_keys("Queena")
first_name.send_keys(Keys.ENTER)

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Song")
last_name.send_keys(Keys.ENTER)

email = driver.find_element_by_name("email")
email.send_keys("queenasong805@gmail.com")
email.send_keys(Keys.ENTER)

sign_in_button = driver.find_element_by_css_selector(".form-signin button")
sign_in_button.click()


# driver.quit()