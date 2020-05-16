### Zadanie domowe z przedmiotu Analiza Systemów Informatycznych

Jedyne co zostało przeniesione z repozytorium repl.it (kod z zajęć) to część kodu w weather.py

W projekcie użyłem pakietów:
* Flask
* Flask-login
* Flask-SQLAlchemy
* Flask-Simple-GeoIP

Funkcjonalności:
* Użytkownik może się zarejestrować. Dane są zapisywane do bazy SQLite
* Użytkownik moze się zalogować
* Użytkownik nie może zarejestrować przy użyciu adresu email, który istnieje już w bazie danych
* Po zalogowaniu wyświetla się pogoda w aktualnym miejscu pobytu użytkownika. W momecie zalogowania pobierane są koordynaty, a następnie na ich podstawie pobierana jest pogoda
* W zakładce Weather użytkownik moze sprawdzić pogodę w dowolnym mieście