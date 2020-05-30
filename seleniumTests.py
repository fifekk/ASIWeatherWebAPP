import string
import barnum
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging
import random
'''
W tym pliku zawarte są testy aplikacji stworzonej w ramach zajęć analiza systemów informatycznych. Wszystkie testy wykorzystują pakiet selenium
'''
# należy odkomentować jedną ze zmiennych driver (w zależności od zainstalowanej przeglądarki) i podać scieżkę do
# pliku webdriver
# driver = webdriver.Chrome()
# driver = webdriver.firefox()
# w zmiennej site_url należy podać adres, gdzie jest uruchomiona aplikacja
site_url = "http://127.0.0.1:5000/"
# przebieg testów jest logowany do apliku app.log, poniższa linijka konfiguruje pakiet logging
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)

# poniższa metoda służy do wygenerowania losowego ciągu znaków
def randomize_string():
    stringLen = 8
    alphabet = string.ascii_letters + string.digits
    return ''.join((random.choice(alphabet) for i in range(stringLen)))

# poniższy test sprawdza czy można zalogować się na nieistniejące konto
def check_if_user_can_login_on_non_existent_account():
    #wygeneruj dane do logowania
    random_email = randomize_string() + '@gmail.com'
    random_password = randomize_string()
    #wejdź na podstonę /login
    driver.get(site_url+"/login")
    #powiększ okno
    driver.maximize_window()
    #znajdź inputy (mail i password)
    email = driver.find_element_by_name("email")
    password = driver.find_element_by_name("password")
    #wyczyść pola
    email.clear()
    password.clear()
    #uzupełnij dane
    email.send_keys(random_email)
    password.send_keys(random_password)
    password.send_keys(Keys.RETURN)
    try:
        #sprawdź czy pojawił się komunikat o błędnych danych
        assert "Please check your login details and try again." in driver.page_source
        logging.info("User couldn't log in with fake credentias")
    except AssertionError:
        logging.info("System allowed user to log in with fake credentials")

# poniższy test sprawdza czy można dwukrotnie zarejestrować się przy użyciu tego samego adresu email
def check_if_user_can_register_two_times_on_the_same_email_address():
    #wygeneruj dane
    email = randomize_string() + '@gmail.com'
    password = randomize_string()
    name = randomize_string()
    #zarejestruj się dwukrotnie przy użyciu tych samych danych
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
        #sprawdź czy pojawił się komunikat o istenijącym koncie
        assert "Email address already exists. Go to login page." not in driver.page_source
        logging.info("User couldn't register two times with the same credentials")
    except AssertionError:
        logging.info("User can register two times with the same credentials")

# poniższy test sprawdza czy WeatherApi działa poprawnie oraz czy użytkownik moze pobrać dane dotyczące prognozy
# pogody dla dowolnego miasta
def check_if_weather_api_works_and_user_can_get_weather_for_given_city():
    #wygeneruj miasto
    city = barnum.create_city_state_zip()[1]
    driver.get(site_url+"weather")
    cityInput = driver.find_element_by_name("city")
    cityInput.send_keys(city)
    cityInput.send_keys(Keys.RETURN)
    try:
        #sprawdź czy są dane z pogodą
        assert city in driver.page_source
        logging.info("WeatherApi works")
    except AssertionError:
        logging.info("Weather api ERROR city: %s", city)

# poniższy test sprawdza czy div z prognozą pogody jest wycentrowany na ekranie full hd, dla mniejszych rozdzielczości
# test nie zadziała
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

# poniższa metoda grupuje wszystie testy
def run_tests():
    check_if_user_can_login_on_non_existent_account()
    check_if_user_can_register_two_times_on_the_same_email_address()
    check_if_weather_api_works_and_user_can_get_weather_for_given_city()
    check_if_div_with_weather_info_is_centered_1920_1080()


run_tests()