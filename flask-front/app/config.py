import os

HOST_IP = os.getenv('HOST_IP', '127.0.0.1')

APP_PORT = int(os.getenv('APP_PORT', '80'))
APP_DEBUG = True if os.getenv('APP_DEBUG', 'true').lower() == 'true' else False

DB_USER = os.getenv('POSTGRES_USER', 'admin')
DB_PASS = os.getenv('POSTGRES_PASSWORD', 'admin')
DB_NAME = os.getenv('POSTGRES_DB', 'postgres')
