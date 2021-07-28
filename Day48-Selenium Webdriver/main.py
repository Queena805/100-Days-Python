from selenium import webdriver
chrome_driver_path = "/Users/queenasong/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")
# price = driver.find_element_by_class_name("price")
# print(price.text)
# driver.close()

# search_bar = driver.find_element_by_name("q")
# print(search_bar.tag_name)

# logo = driver.find_elements_by_class_name("python-logo")

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_times = driver.find_elements_by_css_selector(".event-widget time")
# for time in event_times:
#     print(time.text)

event_names = driver.find_elements_by_css_selector(".event-widget li a")
# for name in event_names:
#     print(name.text)

events_dict = {}
for n in range(len(event_times)):
    events_dict[n] = {
        "time":event_times[n].text,
        "name":event_names[n].text
    }
print(events_dict)


driver.quit()