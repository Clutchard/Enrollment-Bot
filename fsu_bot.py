import getpass
import sys
import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
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

def class_number_search(driver, course_number):
	driver.find_element_by_id("DERIVED_REGFRM1_CLASS_NBR").clear()
	num_field = driver.find_element_by_id("DERIVED_REGFRM1_CLASS_NBR")
	num_field.send_keys(course_number)
	enter_button = driver.find_element_by_id("DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$9$")
	enter_button.click()
	next_button = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("DERIVED_CLS_DTL_NEXT_PB"))
	next_button.click()





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


	else:
		print("Choice 2")





