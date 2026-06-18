# BeatHub 🎵

BeatHub to aplikacja webowa stworzona w Django, umożliwiająca przeglądanie wykonawców, albumów i utworów oraz tworzenie własnych playlist.

## Funkcjonalności

### Użytkownicy

* Rejestracja konta
* Logowanie i wylogowanie
* Publiczne profile użytkowników
* Avatar użytkownika
* Bio użytkownika

### Muzyka

* Lista wykonawców
* Szczegóły wykonawcy
* Lista albumów wykonawcy
* Szczegóły albumu
* Lista utworów albumu
* Wyszukiwarka wykonawców, albumów i utworów

### Playlisty

* Tworzenie playlist
* Usuwanie playlist
* Dodawanie utworów do playlist
* Usuwanie utworów z playlist
* Zmiana kolejności utworów (Move Up / Move Down)

### Panel administratora

* Wyszukiwanie rekordów (`search_fields`)
* Filtrowanie rekordów (`list_filter`)
* Edycja powiązanych modeli (`inlines`)
* Dostosowane listy rekordów (`list_display`)

### Dane testowe

* Generowanie danych przy użyciu Faker
* Własna komenda:

```bash
python manage.py seed_db
```

### Testy

Projekt zawiera podstawowe testy jednostkowe sprawdzające:

* tworzenie modeli
* poprawność działania widoków
* dostęp do chronionych stron

## Technologie

* Python 3.12
* Django 6
* PostgreSQL
* Bootstrap 5
* Faker
* Pillow

## Instalacja

### 1. Klonowanie repozytorium

```bash
git clone <adres_repozytorium>
cd BeatHub
```

### 2. Utworzenie środowiska

Linux:

```bash
python3 -m venv env
source env/bin/activate
```

Windows:

```bash
python -m venv env
env\Scripts\activate
```

### 3. Instalacja zależności

```bash
pip install -r requirements.txt
```

### 4. Konfiguracja pliku .env

Przykład:

```env
DB_NAME=beathub
DB_USER=postgres
DB_PASSWORD=haslo
DB_HOST=localhost
DB_PORT=5432
```

### 5. Migracje

```bash
python manage.py migrate
```

### 6. Utworzenie administratora

```bash
python manage.py createsuperuser
```

### 7. Wygenerowanie danych testowych

```bash
python manage.py seed_db
```

### 8. Uruchomienie serwera

```bash
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem:

```text
http://127.0.0.1:8000/
```

## Dane testowe

Po uruchomieniu:

```bash
python manage.py seed_db
```

tworzeni są przykładowi użytkownicy:

```text
login: user1
hasło: test12345

login: user2
hasło: test12345

login: user3
hasło: test12345
```

## Autor

Marek Berny
