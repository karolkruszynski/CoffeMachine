# CoffeeMachine - PROJECT
Program Automat do kawy pozwala użytkownikowi zamawiać trzy rodzaje kawy: espresso, latte i cappuccino. Użytkownik wprowadza swoje zamówienie, a następnie płaci za kawę. Program oblicza resztę i wydaje napój, jeśli wystarczające ilości składników są dostępne. Użytkownik ma również możliwość sprawdzenia stanu zasobów maszyny oraz zakończenia zamawiania.

Instrukcje obsługi
Uruchomienie programu
Uruchom skrypt "main.py" w terminalu lub IDE.
Wybór kawy
Po uruchomieniu programu, zostanie wyświetlone menu wyboru. Aby wybrać kawę, wpisz "espresso", "latte" lub "cappuccino".
Aby zakończyć zamawianie, wpisz "off".
Aby sprawdzić stan zasobów, wpisz "report".
Płatność
Po wybraniu kawy, zostaniesz poproszony o wprowadzenie monety.
Podaj ilość monet dla każdego rodzaju (quarters, dimes, nickels, pennies) i wprowadź je po kolei w kolejnych linijkach.
Jeśli wprowadzone pieniądze są wystarczające, program wyda kawę i resztę.
Jeśli wprowadzone pieniądze są niewystarczające, program zwróci wprowadzone pieniądze.
Zasoby
Program korzysta z danych dotyczących składników i kosztów kawy z modułu "data.py". Zasoby są zapisane jako słownik w postaci:
```
resources = 
{
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}
```
Koszty kawy są zapisane jako słownik w postaci:
```
MENU = {
    "espresso": {
        "cost": 1.5,
        "ingredients": {
            "water": 50,
            "coffee": 18
        }
    },
    "latte": {
        "cost": 2.5,
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        }
    },
    "cappuccino": {
        "cost": 3.0,
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        }
    }
}
```
