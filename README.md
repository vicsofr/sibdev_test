# Deals Test


## Описание проекта
Тестовое задание, в котором я реализовал два API хэндлера для загрузки, 
обработки и получения данных о пользователях и покупках, которые они совершили. Проект выполнен на Django + Django Rest
Framework. Запускается в Docker + docker-compose, для хранения данных используется СУБД PostgreSQL из контейнера.


## Запуск проекта
Запуск осуществляется командой:
```shell script
docker-compose up
```
- *для просмотра запросов к БД - раскомментировать строку №69 в deals_test/settings.py*

## Описание API
#### 1. [*[POST] /post_deals_csv*](http://0.0.0.0:8000/deals/post_deals_csv) - ссылка

В тело функции получает csv-файл со списком сделок по покупкам камней и записывает данные о сделках в базу (таблица deals).</br>
#### Пример csv-файла приложен в директории проекта ./test_csv 
- *input data*: 
```json
{
  "deals": "file.csv"
}
```
- *result*:
```json
{
  "status": "OK",
  "inserted": 1
}
```
- *error*:
```json
{
  "status": "error",
  "description": "error_desription"
}
```


#### 2. [*[GET] /get_top_clients*](http://0.0.0.0:8000/deals/get_top_clients) - ссылка

При вызове отображает список из 5 клиентов, потративших наибольшую сумму условных единиц за весь период, а также список 
из названий камней, которые купил этот клиент и ещё хотя бы один другой клиент из списка "5 клиентов, потративших наибольшую сумму условных единиц за весь период"
- *result*:
```json
{
  "response": [
    {
      "username": "username",
      "spent_money": 1,
      "gems": ["gem_1", "gem_2"]
    }
  ]
}
```
- *error*:
```json
{
  "status": "error",
  "description": "No data about clients deals. Use POST /post_deals_csv to upload data"
}
```
###### _Python 3.9.5_