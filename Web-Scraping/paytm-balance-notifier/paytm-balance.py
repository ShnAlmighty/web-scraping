from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
import time
import pyttsx3


def SpeakText(command): 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait()

driver = webdriver.Chrome(r"PATH_TO_CHROME_DRIVER_EXE")
driver.get("https://paytm.com/")  
driver.set_window_size(1928,1080)

login=WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_class_name("_1Vt1"))
time.sleep(3)
login.click()

balance = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_class_name("VQt2"))
time.sleep(5)
tempOld = str(balance.text)
tempOld.split()

newPrice="0"
oldPrice=[x for i,x in enumerate(tempOld) if i>2]
oldPrice = ''.join(oldPrice)
# print(oldPrice)
while(True):
    #webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("R").perform()
    driver.refresh()
    temp = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_class_name("VQt2"))
    time.sleep(5)
    # print(temp.text)
    tempNew = str(temp.text) 
    tempNew.split()
    newPrice = [x for i,x in enumerate(tempNew) if i>2]
    newPrice = ''.join(newPrice)
    if(float(newPrice)>float(oldPrice)):
        payment = (float(newPrice)-float(oldPrice))
        print("Money Recieved:",payment)
        say = "{}. rupees. recieved. in paytm. Wallet".format(payment)
        SpeakText(say)
    elif(float(newPrice)<float(oldPrice)):
        payment = (float(oldPrice)-float(newPrice))
        print("Money Deducted:",payment)
        say = "{}. rupees. deducted. from Paytm. Wallet".format(payment)
        SpeakText(say)
    oldPrice=newPrice
