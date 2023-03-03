#### Проект - тестовое задание

#### Поднятие инфраструктуры

Создать образы контейнеров
```bash
docker-compose build
```

Запустить контейнеры с PostgreSQL и Flask-сервером:
```bash
docker-compose up -d
```

Применить миграции к БД:
```bash
docker-compose exec web flask db upgrade
```

WEB сервис работает по эдресу http://localhost:5001/