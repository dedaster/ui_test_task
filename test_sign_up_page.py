import pytest
from selenium.webdriver.common.by import By
import time

# задаем переменные всех вариантов ввода в форму регистрации
@pytest.mark.parametrize(
    "test, mail, name, pas, res",
    [('Test 7 Empty form', '', '', '', 'Sign Up'),
     ('Test 8 Correct new data', 'gg2g@gfg.ru', 'Ken', 'secret', 'Login'),
     ('Test 9 Email form without "@"', 'gg2ggfg.ru', 'Ron', 'bre', 'Sign Up'),
     ('Test 10 Email form without "."', 'gg2g@gfgru', 'Ken', 'secret', 'Sign Up'),
     ('Test 11 Not full Email form', 'gg2g@', 'Ken', 'secret', 'Sign Up'),
     ('Test 12 Double @ in Email form', 'gg2g@g@fg.ru', 'Ken', 'secret', 'Sign Up'),
     ('Test 13 Email form filled with invalid symbols like ","', 'gg2,g@gfg.ru', 'Ken', 'secret', 'Sign Up'),
     ('Test 14 Email form filled with another language (not Latin alphabet)', 'ggрукру2g@dw.ty', 'Ken', 'secret', 'Sign Up'),
     ('Test 15 Name form not filled', 'ggfte2g@g.ttr', '', 'secret', 'Login'),
     ('Test 16 Only Email form', 'gg2g@vebre.tr', '', '', 'Sign Up'),
     ('Test 17 Only Name form', '', 'Ken', '', 'Sign Up'),
     ('Test 18 Only Password form', '', '', 'secret', 'Sign Up'),
     ('Test 19 Data exists', 'gg2g@gfg.ru', 'Ken', 'secret', 'Sign Up')]) 
 
@pytest.mark.regression
@pytest.mark.smoke
# тест проверяет сразу все варианты ввода данных
# показывает на какой странице должен оказаться пользователь после нажатия на кнопку
def test_sign_up_form(browser, test, mail, name, pas, res):
    
    # поиск элементов и приваивание к переменным
    input_email = browser.find_element(By.NAME, "email")
    input_name = browser.find_element(By.NAME, "name")
    input_password = browser.find_element(By.NAME, "password")
    signup_button = browser.find_element(By.CSS_SELECTOR, "button.button")
    
    # Действия с формами ввода
    input_email.send_keys(mail)
    input_name.send_keys(name)
    input_password.send_keys(pas)
    signup_button.click()
    
    # проверка появления ошибки
    title_signup = browser.find_element(By.CLASS_NAME, "title")
    
    assert title_signup.text == res
    
@pytest.mark.regression
# тест проверяет отправку пустой формы
def test_7_empty_form(browser):
    
    # поиск элементов и присваивание к переменным
    signup_button = browser.find_element(By.CSS_SELECTOR, "button.button")

    # Действия с формами ввода
    signup_button.click()
    
    # проверка попадания на страницу авторизации
    title_signup = browser.find_element(By.CLASS_NAME, "title")
    title_error = browser.find_element(By.CLASS_NAME, "is-danger")
    
    assert title_signup.text == "Sign Up"
    assert title_error.text == "Email and Password must be filled"
    
@pytest.mark.regression
@pytest.mark.smoke
# тест проверяет что будет при вводе уже существующих данных
def test_19_data_exists(browser):
    
    # поиск элементов и присваивание к переменным
    input_email = browser.find_element(By.NAME, "email")
    input_name = browser.find_element(By.NAME, "name")
    input_password = browser.find_element(By.NAME, "password")
    signup_button = browser.find_element(By.CSS_SELECTOR, "button.button")
    
    # Действия с формами ввода
    input_email.send_keys("gg2g@gfg.ru")
    input_name.send_keys("Ken")
    input_password.send_keys("secret")
    signup_button.click()
    
    # проверка появления ошибки
    title_signup = browser.find_element(By.CLASS_NAME, "title")
    title_error = browser.find_element(By.CLASS_NAME, "is-danger")
    
    assert title_signup.text == "Sign Up"
    assert title_error.text == "Email address already exists. Go to login page."