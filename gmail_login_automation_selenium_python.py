#WIP file
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import TimeoutException

#Start a Firefox instance and open the webpage
driver = webdriver.Firefox()
driver.get('https://wwww.gmail.com')
sleep(3)

#Find login elements and send values
login_email_address_elem = driver.find_element_by_id('identifierId')
sleep(2)
#myemailid holds the email ID
login_email_address_elem.send_keys(myemailid)

# Submit the form!
driver.find_element_by_class_name('CwaK9').click()
sleep(2)

login_pass_elem = driver.find_element_by_name('password')
#mypassword holds the password of the Gmail acocunt
login_pass_elem.send_keys(mypassword)
sleep(2)


# Submit the form!
driver.find_element_by_class_name('CwaK9').click()
sleep(5)


driver.close()