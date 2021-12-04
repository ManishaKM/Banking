from selenium import webdriver
driver = webdriver.Chrome("../resources/chromedriver.exe")

# from selenium import webdriver
# driver = webdriver.Chrome("../resources/chromedriver.exe")

url = "http://www.google.com"

driver.maximize_window()
driver.get(url)
print(driver.title)
# assert driver.title == "Yahoo"
# assert driver.title == "Google"
assert driver.title == "Google", f"page title {driver.title} did not match the expected title"
print("Thanks")
driver.close()