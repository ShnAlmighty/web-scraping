from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def driverSetup():
    driver = webdriver.Chrome(r"PATH_TO_CHROME_DRIVER.EXE")
    driver.get("https://weather.com/")  
    driver.set_window_size(1200,600)
    return driver

def main(driver,city):
    search_city = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_id("LocationSearch_input"))
    #driver.implicitly_wait(10)
    #ActionChains(driver).move_to_element(search_city).click(search_city).perform()
    search_city.click()
    search_city.send_keys(city)
    time.sleep(5)
    search_city.send_keys(Keys.ENTER)
    time.sleep(5)

    location = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_class_name("CurrentConditions--location--1Ayv3"))
    print("Location: ",location.text)
    
    temperature = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_class_name("CurrentConditions--tempValue--3KcTQ"))
    print("Temperature: ",temperature.text)
    
    precipitaion = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_class_name("CurrentConditions--precipValue--RBVJT"))
    print("Precipitation: ",precipitaion.text)
    
    climate = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_class_name("CurrentConditions--phraseValue--2xXSr"))
    print("Climate: ",climate.text)
    
    forecast =  WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath("//div[@class=\"TodayWeatherCard--TableWrapper--13jpa\"]"))
    print("Forecast: ",forecast.text)

if __name__ == "__main__":
    city = input("Enter city name: ")
    driver = driverSetup()
    main(driver,city)
    again = input("Do you wish to know weather about another city? (yes/no): ")
    while(again.lower() == "yes" or again.lower() == "y"):
        city = input("Enter city name: ")
        if(city):
            main(driver,city)
        else: 
            print("Please enter a city's name")
        again = input("Do you wish to know weather about another city? (yes/no): ")
    driver.close()
