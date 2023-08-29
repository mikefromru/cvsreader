# CSVReader
Веб-сервис на базе django, предоставляющий REST-api. Принимает из POST-запроса .csv файл для обработки. Сохраняет извлеченные из файла данные в БД и возвращает обработанные данные в ответе на GET-запрос.

### Начать
1. Клонировать репозиторий
```
git clone https://github.com/mikefromru/cvsreader.git
```
2. Прейти в папку с проектом
```
cd cvsreader
```
3. Создать виртуальное окружение
```
python3.10 -m venv venv 
``` 
4. Активировать виртуальное окружение
```
source venv/bin/activate
```
5. Для установки зависимостей, выполнить команду
```
pip install -r requirements.txt
```
6. Перейти в директорию project где находится `manage.py` файл 
```
cd project
```
7. Создать файл `.env` в директории `cvsreader/project/project` где находится `settings.py` и добавить переменную окружения
```env
SECRET_KEY=your_secret_key_without_quotation_marks
``` 
8. Создать миграции
```
python manage.py migrate
```
9. Запустить проект
```
python manage.py runserver
```
### Использование
- Получить обработанные данные GET `http://0.0.0.0:800/csv-file`
- Загрузить файл для обработки и добавления в БД POST `http://0.0.0.0:8000/csv-file`
- Можно использовать `client.py` файл для выполнения POST и GET запросов `python client.py`
