from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/Users/queenasong/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


#Get cookie to click on
cookie = driver.find_element_by_id("cookie")

#Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

five_min = time.time() + 5*60   # 5 minutes from now
timeout = time.time() + 5

while True:
    cookie.click()

    #Every 5 sec:
    if time.time() > timeout:
        #Get all upgrade <b> tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        #Convert <b> text into an integer price
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",",""))
                item_prices.append(cost)
        #Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        #Get current cookie count
        money = driver.find_element_by_id("money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)


        #Find upgrade we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id


        #Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        #Add another 5 seconds until the next check
        timeout = time.time() + 5



    #After 5 mins stop the bot and check the cookies

    if time.time() > five_min:
        cookie_per_second = driver.find_element_by_id("cps").text
        print(cookie_per_second)
        break

