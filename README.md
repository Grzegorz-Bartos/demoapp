## 🐳 Uruchomienie w środowisku Docker (najprostsze)

1. Sklonuj repozytorium i przejdź do katalogu projektu.
2. Wykonaj polecenie:

   ```bash
    docker compose up --build
    ```

💡 Po uruchomieniu wejdź w przeglądarce na http://localhost:8000

## 🖥️ Uruchomienie lokalne (bez Dockera)

1. Upewnij się, że masz zainstalowany Python 3.13.
2. Utwórz i aktywuj środowisko wirtualne:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3. (Opcjonalnie) skopiuj plik środowiskowy:

    ```bash
    cp .env.dist .env
    ```

4. Wykonaj migracje i uruchom serwer:

    ```bash
    python src/manage.py migrate
    python src/manage.py runserver
    ```
