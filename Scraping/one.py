#importing webdriver from selenium
from selenium import webdriver


#selecting Firefox as the browser
#in order to select Chrome
# webdriver.Chrome() will be used
userInput=str(input("search what you want"))
driver = webdriver.Chrome()

#URL of the website
url = "https://www.google.com/"

#opening link in the browser
driver.get(url)
# driver.find_element("xpath",'//*[@id="APjFqb"]')
searchInput=driver.find_element("xpath",'//*[@id="APjFqb"]')
# print(searchInput)
searchInput.send_keys(userInput)
searchInput.send_keys(u'\ue007')