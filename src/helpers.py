from faker import Faker
import allure
import requests
import random
import string
import src.data

# Переменная для библиотеки Faker
fake = Faker(['ru_RU'])

# Функция для генерации пароля
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

# Функция для генерации данных пользователя
def generate_user_data():
    return {
        "email": fake.email(),
        "password": generate_random_string(12),
        "name": fake.name()
    }

@allure.step('Регистрация нового пользователя и получение его данных')
def create_user_and_collect_user_data():
    user_data = generate_user_data()
    response = requests.post(src.data.CREATE_USER_URL, data=user_data)
    if response.status_code == 200:
        return user_data
    
@allure.step('Удаление пользователя по токену')
def delete_user(token):
    requests.delete(src.data.DELETE_USER_URL, headers={"Authorization": f'{token}'})