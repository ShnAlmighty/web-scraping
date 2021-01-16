from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def main():
    city = input("Enter city name: ")
   
    driver = webdriver.Chrome(r"C:\Users\L K PATNAIK\Desktop\shantanu\pyth\Web_Automation\Browsers\chromedriver.exe")
    driver.get("https://weather.com/en-IN/")  
    driver.set_window_size(1200,600)

    search_city = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_id("LocationSearch_input"))
    #driver.implicitly_wait(10)
    #ActionChains(driver).move_to_element(search_city).click(search_city).perform()
    search_city.click()
    search_city.send_keys(city)
    time.sleep(5)
    search_city.send_keys(Keys.ENTER)
    time.sleep(5)

    location = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_class_name("CurrentConditions--location--1Ayv3"))
    print(location.text)
    
    temperature = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_class_name("CurrentConditions--tempValue--3KcTQ"))
    print(temperature.text)
    
    precipitaion = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_class_name("CurrentConditions--precipValue--RBVJT"))
    print(precipitaion.text)
    
    climate = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_class_name("CurrentConditions--phraseValue--2xXSr"))
    print(climate.text)
    
    forecast =  WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath("//div[@class=\"TodayWeatherCard--TableWrapper--13jpa\"]"))
    print(forecast.text)
    driver.close()

if __name__ == "__main__":
    main()