import getpass
import sys
import os
import time
from random import randint
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from pathlib import *


def get_credentials():
	username = raw_input("Enter your FsuId: ")
	password = getpass.getpass("Enter your password: ")
	return username, password

def get_class_number():
	x = True
	class_number = raw_input("\nNow enter the numercial class number: ")
	if (class_number.isdigit()):
			x = False
			while x == True:
				class_number = raw_input("\nPlease try again: ")
				if (class_number.isdigit()):
					x = False
	return class_number

def get_class_info():
	print("hello")



def login_function(driver, username, password):
	driver.get("https://cas.fsu.edu/cas/login?service=https%3A%2F%2Fwww.my.fsu.edu%2Fc%2Fportal%2Flogin")
	userfield = driver.find_element_by_name("username")
	passfield = driver.find_element_by_name("password")
	userfield.send_keys(username)
	passfield.send_keys(password)
	login_button = driver.find_element_by_name("submit")
	login_button.click()
	student_center_button = WebDriverWait(driver, 5).until(lambda driver: 
	driver.find_element_by_id("link_icon_200"))

def student_central(driver):
    student_center_button = WebDriverWait(driver, 5).until(lambda driver: 
    driver.find_element_by_id("link_icon_200"))
    student_center_button.click()
    frame = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath("""//*[@id="ptifrmtgtframe"]"""))
    driver.switch_to.frame(frame)
    enroll_button = driver.find_element_by_id("DERIVED_SSS_SCR_SSS_LINK_ANCHOR3")
    enroll_button.click()
    num_field = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("DERIVED_REGFRM1_CLASS_NBR"))

def class_specific_search(driver,course_name,section_number):
	driver.find_element_by_id("DERIVED_REGFRM1_CLASS_NBR").clear()
	search_button = driver.find_element_by_id("DERIVED_REGFRM1_SSR_PB_SRCH")
	search_button.click()

def class_number_search(driver, course_number):
	driver.find_element_by_id("DERIVED_REGFRM1_CLASS_NBR").clear()
	num_field = driver.find_element_by_id("DERIVED_REGFRM1_CLASS_NBR")
	num_field.send_keys(course_number)
	enter_button = driver.find_element_by_id("DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$9$")
	enter_button.click()
	next_button = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("DERIVED_CLS_DTL_NEXT_PB"))
	lab_check(driver)
	next_button = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("DERIVED_CLS_DTL_NEXT_PB"))
	next_button.click()
	next_button2 = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("DERIVED_CLS_DTL_NEXT_PB$280$"))
	next_button2.click()

def shopping_cart(driver):
		proceed_button = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("DERIVED_REGFRM1_LINK_ADD_ENRL$82$"))
		proceed_button.click()
		finish_button = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("DERIVED_REGFRM1_SSR_PB_SUBMIT"))
		finish_button.click()
		table = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("SSR_SS_ERD_ER$scroll$0"))
		image = driver.find_element_by_xpath("""//*[@id="win0divDERIVED_REGFRM1_SSR_STATUS_LONG$0"]/div/img""")
		img_src = image.get_attribute("src")
		if "SUCCESS" in img_src:
			return True
		else:
			startover_button = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("DERIVED_REGFRM1_SSR_LINK_STARTOVER"))
			startover_button.click()
			time.sleep(randint(2,15))
			return False

#This part doesnt work if there is a lab
def lab_check(driver):
	try:
		lab_button = driver.find_element_by_id("SSR_CLS_TBL_RE$sels$0$$0")
		lab_button.click()
		return driver

	except NoSuchElementException:
		return driver





if __name__ == '__main__':

	chrome_path = os.getenv('HOME')+'/chromedriver'
	#path to the downloaded chrome driver

	Continue = raw_input("Welcome to Fsu Class Enrollment Bot\nPress Enter to Continue: \n")

	username, password = get_credentials()
	#gets the user login credentials

	print("\nHow would you like to add the course:\n")
	print("\t1. The four digit class number\n")
	print("\t2. The course name and section number\n")



	#Choice 1 has error check to make sure its a 4 digit number
	choice = raw_input("Please enter your choice: ")
	class_number = ""
	if choice == '1':
		temp = get_class_number()
		class_number = temp
	else:
		course_name = raw_input("Please enter the course name as it appears in student central: ")
		section_number = raw_input("Please enter the section number: ")
	#Gets the user credentials and also gets the way they want to search for the class

	driver = webdriver.Chrome(chrome_path)
	#opens a chrome browser

	while True: 
		try:
			login_function(driver, username, password)
			break
			#trys to login to the fsu website
		except TimeoutException:
			print("\nFsu Credentials incorrect\nTry Again\n")
			username, password = get_credentials()
	#Error occurs if user credentials are wrong or if cant find student central button on new page


	while True:
		try:
			student_central(driver)
			break
		except TimeoutException:
			print("Error: \"Couldn't find Enroll button\"")
			print("Contact Support")
			sys.exit()
	#Error occurs if can't locate the enroll button on the newly loaded page

	if choice == '1':
		while True: 
			try:
				class_number_search(driver, class_number)
				break
				#trys to login to the fsu website
			except TimeoutException:
				print("\nIncorrect Class Number\nTry Again\n")
				class_number = get_class_number()
		loop = False		
		while loop == False:
			try:
				loop = shopping_cart(driver)

			except TimeoutException:
				print("Shopping_cart is Empty")
	else:
		print("Choice 2")
		while True:
			try:
				class_specific_search(driver,course_name,section_number)
				break
			except TimeoutException:
				print("Incorrect course name or section number\nTry Again\n")

		loop = False		
		while loop == False:
			try:
				loop = shopping_cart(driver)

			except TimeoutException:
				print("Shopping_cart is Empty")				



print("You have been enrolled")
