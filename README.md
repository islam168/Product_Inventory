# Проект "Управление предприятиями и продуктами"

Этот проект разработан для управления информацией о предприятиях и продуктах, предоставляя API для выполнения операций CRUD (создание, чтение, обновление, удаление) над данными. Проект реализован с использованием Django Rest Framework для создания API, Docker Compose для контейнеризации приложения и базы данных PostgreSQL, а также интегрирован с Swagger для удобной документации API.

## Инструкции по сборке и запуску

1. Установите Docker и Docker Compose, если они еще не установлены на вашем компьютере. 
Убедитесь чтобы Docker был запущен у вас на компьютере.
2. С клонируйте репозиторий:

    ```
    git clone https://github.com/islam168/Product_Inventory.git
    ```

3. Перейдите в каталог проекта:

    ```
    cd Product_Inventory
    ```

4. Запустите проект с помощью Docker Compose:

    ```
    docker-compose up --build
    ```

Это создаст контейнеры для приложения и базы данных PostgreSQL и запустит их.

## Использование API

API предоставляет следующие конечные точки:

- `/api/enterprises/` - Просмотр списка всех предприятий
- `/api/add_enterprise/` - Создание нового предприятия
- `/api/enterprise/<int:pk>/` - Просмотр, обновления (полное и частичное) и удаление определенной записи
- `/api/categories/` - Просмотр списка всех категорий продуктов
- `/api/add_category/` - Создание новой категории
- `/api/category/<int:pk>/` - Просмотр, обновления (полное и частичное) и удаление определенной записи
- `/api/products/` - Просмотр списка всех продуктов
- `/api/add_product/` - Создание нового продукта
- `/api/product/<int:pk>/` - Просмотр, обновления (полное и частичное) и удаление определенной записи
- `/api/schema/` - создаст JSON-схему API
- `/api/schema/swagger-ui` - создаст документацию Swagger-UI
- `/api/schema/redoc` - предоставляет интерфейс ReDoc для схемы API

### Примеры запросов и ответов:
1. Создание нового предприятия:

   **Запрос:**
    ```
    POST /api/add_enterprise/
   {
       "name": "Enterprise 1",
       "description": "Description of enterprise 1",
       "start_of_workday": "09:00",
       "end_of_workday": "18:00",
       "address": "Address 1"
   }
    ```

    **Ответ:**
    ```json
   {
       "id": 1,
       "name": "Enterprise 1",
       "description": "Description of enterprise 1",
       "start_of_workday": "09:00",
       "end_of_workday": "18:00",
       "address": "Address 1"
   }
    ```

2. Получение списка предприятий:

    **Запрос:**
    ```
    GET /api/enterprises/
    ```

    **Ответ:**
    ```json
    [
        {
            "id": 1,
            "name": "Enterprise 1",
            "description": "Description of enterprise 1",
            "work_hours": "09:00 - 18:00",
            "address": "Address 1"
        },
        {
            "id": 2,
            "name": "Enterprise 2",
            "description": "Description of enterprise 2",
            "work_hours": "08:00 - 17:00",
            "address": "Address 2"
        }
    ]
    ```
    **Чтобы переключиться на другие страницы с записями (Пагинация). Небходимо произвести следующий запрос:**
    ```
    GET /api/enterprises/?page=2 (?page=3, ?page=4 и т.д.).
    ```
    Также c: 
    - /api/products/?page=3 (Просмотр списка всех продуктов)
    - /api/categories/?page=4 (Просмотр списка всех категорий продуктов)

3. Обновление предприятия:

    **Запрос:**
    ```
    PUT /api/enterprise/2/
   {
       "name": "New Enterprise",
       "description": "Description of new enterprise",
       "start_of_workday": "09:00",
       "end_of_workday": "18:00",
       "address": "New Address"
   }
    ```

    **Ответ:**
    ```json
   {
       "id": 2,
       "name": "New Enterprise",
       "description": "Description of new enterprise",
       "start_of_workday": "09:00",
       "end_of_workday": "18:00",
       "address": "New Address"
   }
    ```

4. Удаление предприятия  

   **Запрос:**
    ```
    DELETE /api/enterprise/1/
    ```

    **Ответ в случае ошибки при удалении (Нет такой записи для данного запроса):**
    ```json
   {
       "detail": "No Enterprise matches the given query."
   }
    ```
   **Ответ в случае успешного удаления:**
    ```
   
    ```

5. Создание нового продукта (Перед созданием нового продукта следует создать минимум одно предприятие и одну категорию):

    **Запрос:**
    ```
    POST /api/add_product/
   {
       "name": "Product 1",
       "description": "Product 1",
       "price": "900.80",
       "stock_quantity": 800,
       "category": 1,
       "enterprise": 1
   }
    ```

    **Ответ:**
    ```json
   {
       "id": 1,
       "name": "Product 1",
       "description": "Product 1",
       "price": "900.80",
       "stock_quantity": 800,
       "category": 1,
       "enterprise": 1
   }
    ```

6. Получение определенного продукта:

   **Запрос:**
    ```
    GET /api/enterprise/1/
    ```

    **Ответ:**
    ```json
   {
       "id": 1,
       "name": "Product 1",
       "description": "Product 1",
       "price": "900.80",
       "stock_quantity": 800,
       "category": 1,
       "enterprise": 1
   }
    ```
   
## Модульные тесты

Модульные тесты для API были написаны при помощи ```Pytest```. Их можно найти в каталоге `product_inventory/tests`. Для запуска тестов воспользуйтесь командой:

```
docker-compose exec web pytest
```

## База данных PostgreSQL

Для хранения информации о предприятиях используется PostgreSQL. 
Схема базы данных определена в соответствии с моделями Django. В файле `docker-compose.yml` можно настроить параметры базы данных PostgreSQL по необходимости.
