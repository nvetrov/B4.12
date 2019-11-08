""""
Задание 1
TODO: Напишите модуль users1.py, который регистрирует новых пользователей.
 Скрипт должен запрашивать следующие данные:
имя
фамилию
пол
адрес электронной почты
дату рождения
рост
Все данные о пользователях сохраните в таблице user нашей базы данных sochi_athletes.sqlite3."""

# испортируем модули стандартнй библиотеки uuid и datetime
import uuid
import datetime

# импортируем библиотеку sqlalchemy и некоторые функции из нее
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# константа, указывающая способ соединения с базой данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
# базовый класс моделей таблиц
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = sa.Column(sa.INTEGER, primary_key=True, autoincrement=True)  # идентификатор пользователя, первичный ключ
    first_name = sa.Column(sa.Text)  # имя пользователя
    last_name = sa.Column(sa.Text)  # фамилия пользователя
    gender = sa.Column(sa.TEXT)  # пол
    email = sa.Column(sa.Text)  # адрес электронной почты пользователя
    birthdate = sa.Column(sa.TEXT)  # дату рождения
    height = sa.Column(sa.FLOAT)  # рост


def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии
    """
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()


def request_data():
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    print("Привет! Я запишу твои данные!")
    first_name = input("имя: ")
    last_name = input("фамилию: ")
    gender = input("пол: ")
    email = input("электронная почта: ")
    birthdate = input("дату рождения: ")
    height = float(input("рост: "))
    # user_id = str(uuid.uuid4())
    # создаем нового пользователя
    data = User(
        # id=user_id,
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height

    )
    # возвращаем созданного пользователя
    return data


def main():
    """
    Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    session = connect_db()
    data = request_data()
    session.add(data)
    session.commit()
    print('Данные сохранены')


if __name__ == "__main__":
    main()
