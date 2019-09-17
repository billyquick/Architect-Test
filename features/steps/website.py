from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("C:/Users/Bill/Downloads/chromedriver_win32/chromedriver.exe")

@given('I am on the service-periods page and logged in')
def step_impl_goto_serviceperiods(self):
	username = "qa_user_01"
	password = "HcaR3$!v3%8J"
	driver.get('https://login.stage.transloc.com/login/?next=https://architect.stage.transloc.com/')
	inputUsername = driver.find_element_by_xpath('//*[@id="username"]')
	inputUsername.send_keys(username)
	inputPass = driver.find_element_by_xpath('//*[@id="password"]')
	inputPass.send_keys(password)
	driver.find_element_by_xpath('/html/body/div/div[2]/div/div/form/div[6]/div/div/input').click()
	
@when(u'I click on New Feed on the Service-Periods page')
def step_impl_ClickNewFeed(context):
	try:
		driver.implicitly_wait(5)
		driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div/div[1]/div/div[2]/div/div[2]/a').click()
	except NoSuchElementException:
		pass

@when(u'I click on Save on the New page')
def step_impl_ClickSave(context):
	try:
		driver.implicitly_wait(5)
		driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/button[2]').click()
	except NoSuchElementException:
		pass

@then(u'the submission fails')
def step_impl(context):
	driver.quit()
	pass