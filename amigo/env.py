import os

# Telegram
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Database
DATABASE_URL = os.getenv('DATABASE_URL') or 'sqlite:///database.db'
