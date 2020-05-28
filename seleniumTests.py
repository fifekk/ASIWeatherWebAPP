from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging

driver = webdriver.Chrome("P:\WebDev\Django\ASIWeatherWebApp\chromedriver.exe")
site_url = "http://127.0.0.1:5000/"
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)


def check_if_user_can_login_on_non_existent_account():
    driver.get(site_url+"/login")
    driver.maximize_window()
    # loginButton = driver.find_element_by_xpath("//a[@href=/login]").click()
    email = driver.find_element_by_name("email")
    password = driver.find_element_by_name("password")
    email.clear()
    password.clear()
    email.send_keys("123poaisd@gmail.com")
    password.send_keys("lashdasjdioasd")
    password.send_keys(Keys.RETURN)
    try:
        assert "Please check your login details and try again." in driver.page_source
        logging.info("User couldn't log in with fake credentias")
    except AssertionError:
        logging.info("System allowed user to log in with fake credentials")


def check_if_user_can_register_two_times_on_the_same_email_address():
    email = "jan.kowalski@gmail.com"
    password = "janKowalski123"
    name = "Jan Kowalski"

    for i in range(2):
        driver.get(site_url+"signup")
        driver.maximize_window()
        emailInput = driver.find_element_by_name("email")
        nameInput = driver.find_element_by_name("name")
        passwordInput = driver.find_element_by_name("password")
        emailInput.send_keys(email)
        nameInput.send_keys(name)
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.RETURN)

    try:
        assert "Email address already exists. Go to login page." not in driver.page_source
        logging.info("User couldn't register two times with the same credentials")
    except:
        logging.info("User can register two times with the same credentials")


def check_if_weather_api_works_and_user_can_get_weather_for_given_city(city):
    driver.get(site_url+"weather")
    cityInput = driver.find_element_by_name("city")
    cityInput.send_keys(city)
    cityInput.send_keys(Keys.RETURN)
    try:
        assert city in driver.page_source
        logging.info("WeatherApi works")
    except:
        logging.info("Weather api ERROR city: %s", city)


def check_if_div_with_weather_info_is_centered_1920_1080():
    driver.get(site_url + "weather")
    driver.maximize_window()
    cityInput = driver.find_element_by_name("city")
    cityInput.send_keys("Warszawa")
    cityInput.send_keys(Keys.RETURN)
    divElement = driver.find_element_by_class_name('containerW')
    divSize = divElement.size
    divLocation = divElement.location
    logging.info("WeatherInfo div Location x: {}px y: {}px".format(divLocation['x'], divLocation['y']))
    logging.info("WeatherInfo div Size width: {}px height: {}px".format(divSize['width'], divSize['height']))
    if divLocation['x'] == 472 and divLocation['y'] == 260 and divSize['width'] == 960 and divSize['height'] == 468:
        logging.info("WeatherInfo div is centered in 1920x1080")
    else:
        logging.info("WeatherInfo div is not centered in 1920x1080")
    driver.close()




check_if_user_can_login_on_non_existent_account()
check_if_user_can_register_two_times_on_the_same_email_address()
check_if_weather_api_works_and_user_can_get_weather_for_given_city("asd")
check_if_div_with_weather_info_is_centered_1920_1080()
