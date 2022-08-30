LANG="UTF-8" or "en_US.UTF-8"
LC_ALL="UTF-8" or "en_US.UTF-8"
LC_CTYPE="UTF-8" or "en_US.UTF-8"

from pynput.keyboard import Key , Controller

keyboard = Controller()
mouse = Controller()
import pynput
import mouse
import keyboard






#scraping fire22

from selenium import webdriver
from selenium.webdriver.common.keys	import Keys
import	time


PATH = "C:\External downloads\Microsoft Edge Driver\msedgedriver.exe"
driver = webdriver.Edge(PATH)

driver.get("https://fire22.ag/")

#logging into fire22


username = driver.find_element_by_name("customerID")
username.clear()

username.send_keys("shl153") #


password = driver.find_element_by_name("Password")

password.clear()
password.send_keys("") #password removed for privacy 

time.sleep(3)
login = driver.find_element_by_xpath('/html/body/form/button').click()
driver.maximize_window()
time.sleep(5)


openbets = driver.find_element_by_xpath("/html/body/div[1]/div/header/div[2]/div[2]/div[4]").click()
openbets = driver.find_element_by_xpath("/html/body/div[1]/div/header/div[2]/div[2]/div[4]/div/ul/li[9]/label").click()
time.sleep(3)
openbets = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[1]/div[2]").click()


wager = driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div[2]/div[4]/div[2]/div/div/div[2]/table/tbody')


print(wager.text)


#send wagers to email

import smtplib , ssl

port = 465

sender = "keepbetting.net@gmail.com"
password = "" #password removed for privacy 

receive = sender

message = wager.text

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com" , port , context = context) as server:
	server.login(sender, password)
	message = message.replace("\xbd", " ")
	server.sendmail(sender,receive,message)

print("sent email")