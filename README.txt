Файлы для настройки бота:
bot/.env
docker-compose.yml
keyboards/inline/user/start_keyboards.py

Если нужно отредактировать тексты в боте, то все лежит в файле handlers и keyboards.

В файле bot/alembic.ini в строчке 64 нужно указать свои данные для подключения к бд.(Те, которые вы написали в файле .env!)

Для запуска бота вам необходимо установить докер по любому гайду из интернета. Затем из консоли переходим в папу с файлом "docker-compose"
Вводим:

> docker compose build
> docker compose up -d
> docker exec -it bot bash
> alembic revision --autogenerate
> cd bot/migrations/versions
> ls

Видим список файлов, копируем название файла с набором букв, без расширения!

> cd ..
> cd ..
> alembic upgrade 'тот ключ, что вы скопировали без ковычек!!!'
> exit

С этого момента бот запущен и полностью функционирует
