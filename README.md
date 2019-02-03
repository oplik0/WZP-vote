# Strona do tajnego głosowania

## Jak korzystać (użytkownik):
  Jako użytkownik musisz otrzymać od osoby hostującej indywidualne (przypisane do loginu) hasło do głosowania. 
  To to hasło trafia w pole "Otrzymane hasło". 
  W pole "hasło do szyfrowania" należy wpisać już własne hasło - ważne by je zapamiętać, bo będzie potrzebne do odszyfrowania głosu.
  Dalej wystarczy tylko wpisać swój login i głos w odpowiednie formularze.
  Kiedy zakończy się głosowanie wystarczy podać login i hasło do szyfrowania by odzyskać głos danej osoby.
## Instalacja:
  By zainstalować wystarczy sklonować repozytorium i zainstalować potrzebne moduły. Po kolei:
  ```
  git clone https://github.com/opliko95/WZP-voting-website
  cd WZP-voting-website
  pip install -r requirements.txt
  ```
  Następnie można uruchomić wbudowany serwer flask:
  ```
  python wzp.py
  ```
  Albo zainstalować własny webserver. Jest to zalecane rozwiązane produkcyjne, ponieważ serwer flaska został stworzony jedynie do prostego debuggowania.
  
## Użytkowanie (hosting):
  Strona domyślnie ma włączony zapis, można to przełączyć zmieniając wartość pliku ```writable.txt``` z 1 (zapis) na 0 (odczyt) i vice versa.
  By ustalić hasło dla użytkownika należy wstawić je do pliku
  ```<nazwa_użytkownika>_password.txt```
  Nazwa użytkownika musi być zapisana małymi literami.
  
  Strona zapisuje zaszyfrowane dane w plikach
  ```<nazwa_użytkownika>_vote.txt```
  W czasie gdy jest w stanie zapisu nie działa odczyt, a w trybie odczytu nie może zapisywać danych.
