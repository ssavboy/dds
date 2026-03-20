# Cash Flow Manager (ДДС)

Небольшое Django‑приложение для учёта движения денежных средств: создание, просмотр, редактирование и удаление операций с фильтрами по дате, статусу, типу, категории и подкатегории.

***

<img width="1339" height="559" alt="image" src="https://github.com/user-attachments/assets/b8025b7a-c771-4122-b1fe-0ccbfc4ca33c" />


## Запуск через venv

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

***

## Запуск через Poetry

```bash
poetry install
poetry run python manage.py migrate
poetry run python manage.py runserver
```

Главная страница: `http://127.0.0.1:8000/`
Админка (управление справочниками): `http://127.0.0.1:8000/admin/`.

***

## Начальные данные (initial_dds_data.json)

После миграций можно загрузить базовые статусы, типы, категории и подкатегории.

Через venv:

```bash
python manage.py loaddata fixtures/initial_dds_data.json
```

Через Poetry:

```bash
poetry run python manage.py loaddata fixtures/initial_dds_data.json
```

После этого в форме создания записи будут доступны значения из задания (Бизнес/Личное/Налог, Пополнение/Списание, Инфраструктура/Маркетинг и т.п.).
***

## pre-commit

В проекте настроен pre-commit с форматированием и линтингом (black, flake8).

Установка хуков:

Через venv:

```bash
pip install pre-commit
pre-commit install
```

Через Poetry:

```bash
poetry run pre-commit install
```

Запустить проверки вручную для всех файлов:

```bash
pre-commit run --all-files
# или
poetry run pre-commit run --all-files
```
