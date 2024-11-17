## Проект it-solutions-cars - сайт с автомобилями, тестовое задание для It-solutions.

### Возможности проекта:
- Регистрация, аутентификация и авторизация пользователей
- Публикация записей об автомобилях
- Комментарии к записям других авторов.

### Возможности API:
- Получение, создание, обновление, удаление записей.
- Получение, создание комментариев.
- Получение, обновление и проверка токена авторизации (JWT).

Redoc API: your-domain/api/schema/redoc/
<br>

### Технологии
![Python](https://img.shields.io/badge/Python-3.10-%23254F72?style=flat-square&logo=python&logoColor=yellow&labelColor=254f72)
![Django](https://img.shields.io/badge/Django-5.1.3-0C4B33?style=flat-square&logo=django&logoColor=white&labelColor=0C4B33)
![Django](https://img.shields.io/badge/Django%20REST-3.15.2-802D2D?style=flat-square&logo=django&logoColor=white&labelColor=802D2D)


### Как запустить проект:

Клонировать репозиторий

```
git clone https://github.com/G-Star29/it-solutions-cars
```
Установка зависимостей:

```
pip install -r requirements.txt
```

Перейдите в директорию:
```
cd it-solutions-cars/it-solutions-cars/
```

Примените миграции:

```
python manage.py migrate
```

Соберите статику:

```
python manage.py collectstatic --no-input
```


Запуск тестового сервера:

```
python manage.py runserver
```
