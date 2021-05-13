import os

# Telegram
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_FATHER_ID = int(os.getenv('TELEGRAM_FATHER_ID') or 0)

# Database
DATABASE_URL = os.getenv('DATABASE_URL') or 'sqlite:///database.db'
