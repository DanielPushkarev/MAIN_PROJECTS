## Pereval-API

### Описание проекта

API мобильного приложения Федерации Спортивного Туризма России (ФСТР) с помощью Django Rest Framework. 

### Стек технологий 

В ходе создания проекта применялись различные инстументы и технологии. Они представлены ниже:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

## Документация для Эндпоинтов 

All URIs are relative to */*

| Class           | Method                                                                               | HTTP request                                 | Description                              |
|-----------------|--------------------------------------------------------------------------------------|----------------------------------------------|------------------------------------------|
| *SubmitDataApi* | [**submit_data_create**](docs/SubmitDataApi.md#submit_data_create)                   | **POST** /submitData                         | Добавление перевала                      |
| *SubmitDataApi* | [**submit_data_partial_update**](docs/SubmitDataApi.md#submit_data_partial_update)   | **PATCH** /submitData/{id}/                  | Редактирование перевала                  |
| *SubmitDataApi* | [**submit_data_retrieve**](docs/SubmitDataApi.md#submit_data_retrieve)               | **GET** /submitData/{id}/                    | Извлечение данных о перевале             |
| *SubmitDataApi* | [**submit_data_user_email_list**](docs/SubmitDataApi.md#submit_data_user_email_list) | **GET** /submitData/user__email&#x3D;{email} | Извлечение списка перевалов пользователя |
