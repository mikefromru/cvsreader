# CSVReader
Веб-сервис на базе django, предоставляющий REST-api. Принимает из POST-запроса .csv файл для обработки. Сохраняет извлеченные из файла данные в БД и возвращает обработанные данные в ответе на GET-запрос.

### Начать
1. Склонировать репозиторий
```
git clone https://github.com/mikefromru/cvsreader.git
```
2. Прейдите в папку с проектом
```
cd cvsreader
```
3. Для установки зависимостей, выполните коману
```
pip install -r requirements.txt
```

###Использование
- Получить обработанные данные GET `http://0.0.0.0:800/csv-file`
- Загрузить файл для обработки и добавления в БД POST `http://0.0.0.0:8000/csv-file`
