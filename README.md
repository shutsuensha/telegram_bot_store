## Установка и запуск проекта
```bash
git clone https://github.com/shutsuensha/telegram_bot_store.git
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 run.py
```
## Настройка
добавьте переменные окружения в .env file:
TOKEN=
SQLALCHEMY_URL=sqlite+aiosqlite:///file_path
