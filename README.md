# Python API Integrator

**Универсальный Python-клиент для REST API с retry, backoff, Pydantic-валидацией**

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Описание

Готовый к продакшену HTTP-клиент с:
- Автоматическими retry и exponential backoff (tenacity)
- Pydantic-валидацией ответов
- Асинхронным интерфейсом (httpx)
- Конфигурацией через .env

---

## Быстрый старт
`ash
git clone https://github.com/Shamanchi/python-api-integrator
cd python-api-integrator
cp .env.example .env
docker-compose up -d
`

### Переменные окружения
| Переменная | Описание |
|------------|----------|
| API_BASE_URL | Базовый URL API |
| API_KEY | API ключ |
| API_TIMEOUT | Таймаут (сек) |
| RETRY_ATTEMPTS | Кол-во попыток |
| RETRY_BACKOFF | Множитель backoff |

---

## Использование
`python
from app.services.client import APIClient

async with APIClient() as client:
    users = await client.get('/users')
    new_user = await client.post('/users', {'name': 'John'})
`

---

## Тесты
`ash
pytest -v
`

---

## Docker
`ash
docker build -t python-api-integrator .
docker-compose up -d
`

---

## Структура
`
├── app/
│   ├── api/routes.py
│   ├── core/config.py
│   ├── core/logging.py
│   ├── services/client.py
│   └── main.py
├── tests/test_api.py
├── .github/workflows/ci.yml
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
`

---

## CI/CD
GitHub Actions: Ruff, MyPy, Pytest, Docker build

---

## Лицензия
MIT

---

> Источник темы: Каталог портфолио, запись python-api-integrator