### Zadanie domowe z przedmiotu Analiza Systemów Informatycznych

Jedyne co zostało przeniesione z repozytorium repl.it (kod z zajęć) to część kodu w weather.py

W projekcie użyłem pakietów:
* Flask
* Flask-login
* Flask-SQLAlchemy
* Flask-Simple-GeoIP
* Barnum
* Selenium

Funkcjonalności:
* Użytkownik może się zarejestrować. Dane są zapisywane do bazy SQLite
* Użytkownik moze się zalogować
* Użytkownik nie może zarejestrować przy użyciu adresu email, który istnieje już w bazie danych
* Po zalogowaniu wyświetla się pogoda w aktualnym miejscu pobytu użytkownika. W momecie zalogowania pobierane są koordynaty, a następnie na ich podstawie pobierana jest pogoda
* W zakładce Weather użytkownik moze sprawdzić pogodę w dowolnym mieście

Testowanie
* W pliku seleniumTests.py znajdują się testy
* W pliku app.log znajdują się logi z wykonanych testów
* Aby uruchomić testy należy: 
    * Zainstalować pakiet barnum i selenium
    * Pobrać selenium webdriver
    * W pliku seleniumTests.py uzupełnić wartości dla zmiennych
    * Uruchomić aplikacje
    * Uruchomić plik seleniumTests.py
    