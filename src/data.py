# URL сайта "Stellar Burgers"
BASE_URL = 'https://stellarburgers.nomoreparties.site'

# API - Пользователь
# URLы API для функциональности пользователя
CREATE_USER_URL = BASE_URL + '/api/auth/register'
LOGIN_USER_URL = BASE_URL + '/api/auth/login'
UPDATE_USER_DATA_URL = BASE_URL + '/api/auth/user'
DELETE_USER_URL = BASE_URL + '/api/auth/user'

# Системные сообщения для функциональности пользователя
# Создание пользователя
USER_CREATED_MESSAGE = 'success":true'
USER_EXISTS_MESSAGE = 'message":"User already exists'
MISSING_FIELDS_IN_USER_FORM_MESSAGE = 'message":"Email, password and name are required fields'

# Логин пользователя
USER_LOGIN_MESSAGE = 'success":true'
USER_NOT_FOUND_MESSAGE = 'message":"email or password are incorrect'

# Обновление данных пользователя
USER_DATA_UPDATED_MESSAGE = 'success":true'
USER_DATA_NOT_UPDATED_DUE_LOGIN_MESSAGE = 'message":"You should be authorised'
USER_DATA_NOT_UPDATED_DUE_EMAIL_MESSAGE = 'message":"User with such email already exists'


# API - Заказы
# URLы API для функциональности заказов
CREATE_ORDER_URL = BASE_URL + '/api/orders'
GET_ORDERS_URL = BASE_URL + '/api/orders'

# Системные сообщения для функциональности заказов
# Создание заказа
ORDER_CREATED_MESSAGE = 'success":true'
ORDER_CREATE_WITHOUT_INGREDIENTS_MESSAGE = 'message":"Ingredient ids must be provided'
ORDER_CREATE_WITH_INCORRECT_INGREDIENTS_MESSAGE = 'Internal Server Error'

# Получение заказов
ORDER_GET_SUCCEED_MESSAGE = 'success":true'
ORDER_DONT_GET_DUE_LOGIN_MESSAGE = '"message":"You should be authorised"'

# ID ингредиентов
CRATER_BUN_ID = '61c0c5a71d1f82001bdaaa6c'
CHEESE_MAIN_ID = '61c0c5a71d1f82001bdaaa7a'
FILLET_MAIN_ID = '61c0c5a71d1f82001bdaaa6e'
SPICY_SAUCE_ID = '61c0c5a71d1f82001bdaaa72'