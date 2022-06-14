from selenium import webdriver

points_range = range(1, 1000)

def test_scores_service():
    my_driver = webdriver.Chrome(executable_path="/Users/danielbenharosh/Downloads/chromedriver") 
    my_driver.get('http://127.0.0.1:30000/Score_Read')
    element =  my_driver.find_element_by_id('score').text
    # print (element)
    element = int(element)
    if element in points_range:
        return 1
    else:
        return 0     

test_score = test_scores_service()
# print(bool(test_score))

def main_function():
    if test_score == True:
        print(0)
    else:
        print(-1)    
    
main_function()

