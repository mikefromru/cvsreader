# CSVReader
Веб-сервис на базе django, предоставляющий REST-api. Принимает из POST-запроса .csv файл для обработки. Сохраняет извлеченные из файла данные в БД и возвращает обработанные данные в ответе на GET-запрос.
### Технологии
- Django
- Django REST Framework
- Docker
- Docker compose
- Postgres
### Начать
1. Клонировать репозиторий
```
git clone https://github.com/mikefromru/cvsreader.git
```
2. Прейти в папку с проектом
```
cd cvsreader
```
3. Переименовать файл `.env.EXAMPLE` в `.env` который находится в каталоге `project/project`

4. Из корня проекта где находится `Dockerfile` запустить команду
```
docker-compose --env-file project/project/.env up 
```
### Использование
- Получить обработанные данные GET `http://0.0.0.0:800/csv-file`
- Загрузить файл для обработки и добавления в БД POST `http://0.0.0.0:8000/csv-file`
- Можно воспользоваться `client.py` который находится в `project/client.py` файл для выполнения POST и GET запросов `python client.py`. Это консольная программа с простым интерфейсом. 
##### Зависимости для консольной программы `client.py` 
```
pip install requests simple_term_menu art
```

