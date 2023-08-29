# CSVReader
Веб-сервис на базе django, предоставляющий REST-api. Принимает из POST-запроса .csv файл для обработки. Сохраняет извлеченные из файла данные в БД и возвращает обработанные данные в ответе на GET-запрос.

### Начать
1. Склонировать репозиторий
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
source env/bin/activate
```
5. Для установки зависимостей, выполнить команду
```
pip install -r requirements.txt
```
6. Создать файл `.env` в директории `cvsreader/project` и добавить переменную окружения
```env
SECRET_KEY=your_secret_key_without_quotation_marks
```
7. Создать миграции
```
python manage.py migrate
```
8. Запустить проект
```
python manage.py runserver
```

### Использование
- Получить обработанные данные GET `http://0.0.0.0:800/csv-file`
- Загрузить файл для обработки и добавления в БД POST `http://0.0.0.0:8000/csv-file`
