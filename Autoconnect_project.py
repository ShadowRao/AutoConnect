from selenium_firefox import Firefox
from selenium import webdriver
import geckodriver_autoinstaller
import time
import schedule

#Credentials
username = ""
password = ""

def Autoconnect():
    # Import the firefox Webdriver, with the pre-configured option
    driver = webdriver.Firefox(executable_path="Enter path to geckodriver.exe here")

    # Sign In and username
    driver.get("https://www.google.com")
    Sign_in =driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[2]/a").click()
    Username_Box = driver.find_element_by_xpath("//*[@id='identifierId']")
    Username_Box.send_keys(username)
    
    #Click next
    Next = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
    time.sleep(5)

    #Typing Password
    Pass_Box = driver.find_element_by_css_selector("#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    Pass_Box.send_keys(password)
    time.sleep(3)

    #Click Next Again
    Next2 =driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()

    #Go to meet
    driver.get("https://meet.google.com/sxw-mojp-ptz")
    time.sleep(5)
    
    #Switch Off Cam
    driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div").click()
    

    #Mute Mic
    Mic = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div").click()

    #Joining the Meet
    Join = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div/div[1]/span/span").click()

    # Wait a while for the account to get locked again
    #time.sleep(1000)

schedule.every().day.at("18:23").do(Autoconnect)

while True:
    schedule.run_pending()
    time.sleep(1)