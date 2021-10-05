from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\ranji\\Downloads\\All Softwares\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")


driver.find_element_by_css_selector("a[href*='shop']").click()
# driver.find_element_by_link_text("Shop").click()

products = driver.find_elements_by_xpath("//div[@class ='card h-100']")

#refer waitDemoExplicit.py  Button in buttons
# //div[@class ='card h-100']/div/h4/a
# products =//div[@class ='card h-100']
# product names = div/h4/a
# buttons = div[@class ='card h-100']/div[2]/button

for product in products:
	# print(product.find_element_by_xpath("div/h4/a").text) print the all the product
	productName = product.find_element_by_xpath("div/h4/a").text
	if productName == "Blackberry":
		#Add item to car
		product.find_element_by_xpath("div/button").click()
#click on checkout button
driver.find_element_by_css_selector('a[class*="btn-primary" ]').click()
#clcik on final checkout
driver.find_element_by_css_selector("button[class*='btn-success' ]").click()
#enter key as Ind -location
driver.find_element_by_css_selector("#country").send_keys("Ind")


wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

driver.find_element_by_link_text("India").click ()

#click on checkbox
driver.find_element_by_xpath("//div[@class ='checkbox checkbox-primary']").click()
#click on submit button
driver.find_element_by_css_selector("[type = 'submit']").click()
#print message
print(driver.find_element_by_css_selector("div[class*='alert-dismissible']").text)
#validate message
successText = driver.find_element_by_css_selector("div[class*='alert-dismissible'").text

assert "Success! Thank you!" in successText
#take screenshot
driver.get_screenshot_as_file("screen.png")
