# Импорты
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Путь к базе
DB_PATH = 'sqlite:///albums.sqlite3'

# Создаем базовый класс
Base = declarative_base()



class Album(Base):
    """
    Описывает структуру таблицы album для хранения записей музыкальной библиотеки
    """
    __tablename__ = 'album'

    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)

def connect_db(path):
    """    Устанавливает соединение к базе данных,
    создает таблицы, если их еще нет и возвращает объект сессии
    """
    endine = sa.co
