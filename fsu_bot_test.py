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
	username = raw_input("Enter your FSUID: ")
	password = getpass.getpass("Enter your password: ")
	return username, password

def get_class_number():
	class_number = raw_input("\nNow enter the numercial class number: ")
	if not(class_number.isdigit()):
			while True:
				class_number = raw_input("\nPlease try again: ")
				if (class_number.isdigit()):
					break
	return class_number

def get_class_info():
	course_name = raw_input("Please enter the course abrevation(Ex: cop) : ")
	if not(course_name.isalpha() and len(course_name) == 3):
		while True:
			course_name = raw_input("\nPlease try again: ")
			if (course_name.isalpha() and len(course_name) == 3):
				break

	course_number = raw_input("Please enter the course number: ")
	if not(course_number.isdigit()):
			while True:
				course_number = raw_input("\nPlease try again: ")
				if (course_number.isdigit()):
					break	
	return course_name, course_number


def login_function(driver, username, password):
	driver.get("https://cas.fsu.edu/cas/login?service=https%3A%2F%2Fwww.my.fsu.edu%2Fc%2Fportal%2Flogin")
	userfield = driver.find_element_by_name("username")
	passfield = driver.find_element_by_name("password")
	userfield.send_keys(username)
	passfield.send_keys(password)
	login_button = driver.find_element_by_name("submit")
	login_button.click()
	student_center_button = WebDriverWait(driver, 10).until(lambda driver: 
	driver.find_element_by_id("link_icon_200"))

def student_central(driver):
    student_center_button = WebDriverWait(driver, 10).until(lambda driver: 
    driver.find_element_by_id("link_icon_200"))
    student_center_button.click()
    frame = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("""//*[@id="ptifrmtgtframe"]"""))
    driver.switch_to.frame(frame)
    enroll_button = driver.find_element_by_id("DERIVED_SSS_SCR_SSS_LINK_ANCHOR3")
    enroll_button.click()
    num_field = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("DERIVED_REGFRM1_CLASS_NBR"))

def class_specific_search(driver, course_name, course_number):
	coursefield = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("SSR_CLSRCH_WRK_SUBJECT$2"))
	coursefield.clear()
	coursefield.send_keys(course_name)

	coursenumfield = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("SSR_CLSRCH_WRK_CATALOG_NBR$3"))
	coursenumfield.clear()
	coursenumfield.send_keys(course_number)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(5)
	search_button1 = driver.find_element_by_xpath("""//*[@id="CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH"]""")
	search_button1.click()
	counter = 0	
	class_time =  WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("MTG_DAYTIME$" + str(counter)))
	while True:
		try:

			class_time =  WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("MTG_DAYTIME$" + str(counter)))
			class_room =  WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("MTG_ROOM$" + str(counter)))
			class_instructor = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("MTG_INSTR$" + str(counter)))
			counter = counter + 1
		
			class_time_text = class_time.text
			class_room_text = class_room.text
			class_instructor_text = class_instructor.text
		
			print("\nOption: " + str(counter))
			print("****************************************")
			print("Class Time:\n" + class_time_text + "\n")
			print("Class Room:\n" + class_room_text + "\n")
			print("Class Instructor:\n" + class_instructor_text)
			print("****************************************")
		except TimeoutException:
			break

	option = raw_input("Which class would you like to add? Please select an option: ")
	print ("Press CTRL + C to cancel at anytime")
	select_button1 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("SSR_PB_SELECT$" + str(int(option)-1)))
	select_button1.click()

	next_button2 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("DERIVED_CLS_DTL_NEXT_PB$280$"))
	next_button2.click()
	



def class_number_search(driver, course_number):
	if counter == 0:
		print ("Press CTRL + C to cancel at anytime")
	driver.find_element_by_id("DERIVED_REGFRM1_CLASS_NBR").clear()
	num_field = driver.find_element_by_id("DERIVED_REGFRM1_CLASS_NBR")
	num_field.send_keys(course_number)
	enter_button = driver.find_element_by_id("DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$9$")
	enter_button.click()
	next_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("DERIVED_CLS_DTL_NEXT_PB"))
	driver = lab_check(driver)
	#doesn't work with a lab
	next_button1 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("DERIVED_CLS_DTL_NEXT_PB"))
	next_button1.click()
	next_button2 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("DERIVED_CLS_DTL_NEXT_PB$280$"))
	next_button2.click()


def shopping_cart(driver):
		proceed_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("DERIVED_REGFRM1_LINK_ADD_ENRL$82$"))
		proceed_button.click()
		finish_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("DERIVED_REGFRM1_SSR_PB_SUBMIT"))
		finish_button.click()
		table = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("SSR_SS_ERD_ER$scroll$0"))
		image = driver.find_element_by_xpath("""//*[@id="win0divDERIVED_REGFRM1_SSR_STATUS_LONG$0"]/div/img""")
		img_src = image.get_attribute("src")
		if "SUCCESS" in img_src:
			return True
		else:
			startover_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("DERIVED_REGFRM1_SSR_LINK_STARTOVER"))
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

	Continue = raw_input("Welcome to the Fsu Class Enrollment Bot\nCaution: Please be certain of the desired class details before running the Bot.\nPress \"Enter\" to Continue: \n")

	username, password = get_credentials()
	#gets the user login credentials

	print("\nHow would you like to add the course:\n")
	print("\t1. The specific class number\n")
	print("\t2. The course name and section number\n")
	print("\t3. The course is already in shopping cart\n")



	choice = raw_input("Please enter your choice: ")
	while choice not in ['1', '2', '3']:
		print("Choice is invalid. Please try again.")
		choice = raw_input("Please enter your choice: ")
		if choice == '1':
			break
		if choice == '2':
			break
		if choice == '3':
			break

	class_number = ""
	course_name = ""
	course_number = ""
	if choice == '1':
		temp = get_class_number()
		class_number = temp
	elif choice == '2':
		temp = get_class_info()
		course_name, course_number = temp
		
	#Gets the user credentials and also gets the way they want to search for the class

	driver = webdriver.Chrome(chrome_path)
	#opens a chrome browser

	while True: 
		try:
			login_function(driver, username, password)
			break
			#trys to login to the fsu website
		except TimeoutException:
			print("\nFsu Credentials incorrect.\nPlease try again.\n")
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

	counter = 0		#Counter so I can print to the screen a specific message only once.
	if choice == '1':
		while True: 
			try:
				class_number_search(driver, class_number)
				counter += 1
				break
				#trys to login to the fsu website
			except TimeoutException:
				print("\nIncorrect Class Number.\nPlease try again.\n")
				class_number = get_class_number()
		loop = False		
		while loop == False:
			try:
				loop = shopping_cart(driver)

			except TimeoutException:
				print("Shopping_cart is Empty")
	elif choice == '2':
		search_button = driver.find_element_by_id("DERIVED_REGFRM1_SSR_PB_SRCH")
		search_button.click()
		check_box = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("SSR_CLSRCH_WRK_SSR_OPEN_ONLY_LBL$8"))
		check_box.click()
		while True:
			try:
				class_specific_search(driver, course_name, course_number)
				break
			except TimeoutException:
				print("\nIncorrect course name or section number\nTry Again\n")
				course_name, course_number = get_class_info()

		loop = False		
		while loop == False:
			try:
				loop = shopping_cart(driver)

			except TimeoutException:
				print("Shopping_cart is Empty")		
	else:
		loop = False		
		while loop == False:
			try:
				loop = shopping_cart(driver)

			except TimeoutException:
				print("Shopping_cart is Empty")
				print("Please put class in shopping cart")
				sys.exit()

print("You have been enrolled")
