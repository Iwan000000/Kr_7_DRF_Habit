Проект "Управление привычками"
Этот проект представляет собой API для управления привычками с использованием Django и Django Rest Framework.

Установка
1. Склонируйте репозиторий на ваш компьютер:

Копировать

    git clone https://github.com/Iwan000000/Kr_7_DRF_Habit.git

2. Установите необходимые зависимости:


    pip install -r requirements.txt

3. Примените миграции:


    python manage.py migrate

4. Запустите сервер:


    python manage.py runserver

Использование
API для управления привычками и приятными привычками пользователей.

Эндпоинты:
Создание новой привычки
- POST /habits/create/

- Позволяет создать новую привычку.

Просмотр всех привычек пользователя
- GET /habits/list/

- Позволяет просмотреть все привычки текущего пользователя.

Просмотр всех публичных привычек
- GET /habits/public/

- Позволяет просмотреть все публичные привычки.

Обновление привычки
- PUT /habits/update/<id>/

- Позволяет обновить определенную привычку.

Удаление привычки
- DELETE /habits/delete/<id>/

- Позволяет удалить определенную привычку.

Просмотр привычки
- GET /habits/detail/<id>/

- Позволяет просмотреть детали определенной привычки.

Создание новой приятной привычки
- POST /nicehabits/create/

- Позволяет создать новую приятную привычку.

Просмотр приятной привычки
- GET /nicehabits/detail/<id>/

- Позволяет просмотреть детали определенной приятной привычки.

Обновление приятной привычки
- PUT /nicehabits/update/<id>/

- Позволяет обновить определенную приятную привычку.

Удаление приятной привычки
- DELETE /nicehabits/delete/<id>/

- Позволяет удалить определенную приятную привычку.

Просмотр всех приятных привычек пользователя
- GET /nicehabits/list/

- Позволяет просмотреть все приятные привычки текущего пользователя.

Авторизация

Все эндпоинты требуют авторизации. Токен необходимо передавать в заголовке Authorization с префиксом Token.

Пагинация

Результаты возвращаются с пагинацией по умолчанию 5 элементов на страницу.
API требует аутентификации, поэтому вам нужно будет авторизоваться, чтобы взаимодействовать с привычками. Вы можете использовать токены доступа для этого.

Документация API

Документация API доступна после запуска сервера по адресу: http://localhost:8000/redoc/ или http://localhost:8000/docs/

Развертывание приложения
Перед развертыванием приложения убедитесь, что у вас установлены следующие компоненты:

    Docker

    Docker Compose



Шаг 1: Настройка переменных окружения
Создайте файл (.env) в корневой директории проекта и заполните его переменными окружения:


    POSTGRES_DB=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_HOST=
    POSTGRES_PORT=
    SUPER_USER=
    SUPER_USER_PASS=
    SECRET_KEY=
    REDIS_URL=
    TELEGRAM_BOT_API_KEY=

Шаг 2: Запуск Docker-контейнеров
Перейдите в корневую директорию проекта и запустите Docker-контейнеры с помощью Docker Compose:


    cd /path/to/your/project
    docker-compose up -d

Опция -d позволяет запустить контейнеры в фоновом режиме.

Шаг 3: Применение миграций
После запуска контейнеров приложению необходимо применить миграции базы данных. Для этого выполните следующую команду внутри контейнера Django:


    docker-compose exec app python manage.py migrate

Шаг 4: Запуск приложения
Теперь приложение должно быть готово к использованию. Вы можете открыть браузер и перейти по адресу http://localhost:8000, чтобы увидеть приложение.

Шаг 5: Остановка и удаление контейнеров
Чтобы остановить и удалить контейнеры, выполните следующую команду в корневой директории проекта:


    docker-compose down

Эта команда остановит и удалит все контейнеры, сети и тома, которые были созданы при запуске Docker Compose.


Дополнительная информация
Этот проект был создан в учебных целях для демонстрации работы с Django и Django Rest Framework. Не используйте его в продакшене без необходимой настройки и безопасности.
