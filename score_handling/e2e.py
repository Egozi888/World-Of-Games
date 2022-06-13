from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


my_driver = webdriver.Chrome(executable_path="/Users/danielbenharosh/Downloads/chromedriver") 
my_driver.get('http://127.0.0.1:30000/Score_Read')
element =  my_driver.find_element_by_id('score').text

# print("Value of input box: " + element.get_attribute('value'))
# print(element.get_attribute('80'))
print (element)

element = int(element) + 4

print (element)
    

# def test_scores_service():





# urls = ['http://www.ynet.co.il','https://mako.co.il']
# my_driver.get(urls[0])