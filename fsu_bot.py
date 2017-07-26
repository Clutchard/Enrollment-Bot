import getpass
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
chrome_path = r"/home/clutchard/chromedriver_linux64/chromedriver"
Continue = raw_input("Welcome to Fsu Class Enrollment Bot\nPress Enter to Continue\n")
username = raw_input("Enter your FsuId: ")
password = getpass.getpass("Enter your password: ")
print("\nHow would you like to add the course\n")
print("1. The four digit class number\n")
print("2. The course name and section number\n")
choice = raw_input("Please enter your choice: ")


driver = webdriver.Chrome(chrome_path)
driver.get("https://cas.fsu.edu/cas/login?service=https%3A%2F%2Fwww.my.fsu.edu%2Fc%2Fportal%2Flogin")
userfield = driver.find_element_by_name("username")
passfield = driver.find_element_by_name("password")
userfield.send_keys(username)
passfield.send_keys(password)
login_button = driver.find_element_by_name("submit")
login_button.click()

student_center_button = WebDriverWait(driver, 10).until(lambda driver: 
driver.find_element_by_id("link_icon_200"))
student_center_button.click()
#enroll_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("""//*[@id="DERIVED_SSS_SCR_SSS_LINK_ANCHOR3"]"""))
driver.implicitly_wait(5)
enroll_button = driver.find_element_by_xpath("""//*[@id="DERIVED_SSS_SCR_SSS_LINK_ANCHOR3"]""")
enroll_button.click()
