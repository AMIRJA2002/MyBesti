# Aury

یک پروژه FastAPI با ساختار مشابه Django، MongoDB و Telegram Driver

## ویژگی‌ها

- FastAPI 0.115.0
- Python 3.13
- MongoDB با Motor (async driver)
- python-telegram-bot برای ارتباط با Telegram
- ساختار مشابه Django
- Docker و Docker Compose
- مدیریت تنظیمات با Pydantic Settings

## ساختار پروژه

```
.
├── core/
│   ├── settings/
│   │   ├── __init__.py
│   │   └── base.py
│   ├── __init__.py
│   ├── database.py
│   └── telegram.py
├── api/
│   └── v1/
│       ├── endpoints/
│       │   ├── __init__.py
│       │   └── health.py
│       ├── __init__.py
│       └── router.py
├── users/
│   ├── __init__.py
│   ├── handlers.py
│   ├── models.py
│   ├── schemas.py
│   └── services.py
├── telegram_app/
│   ├── services/
│   │   ├── __init__.py
│   │   └── telegram_handler.py
│   ├── examples/
│   │   ├── __init__.py
│   │   └── usage_example.py
│   └── __init__.py
├── main.py
├── manage.py
├── .env
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

## نصب و راه‌اندازی

### با Docker

1. تنظیمات Telegram را در `.env` وارد کنید

2. پروژه را اجرا کنید:
```bash
docker-compose up -d
```

### بدون Docker

1. محیط مجازی بسازید:
```bash
python3.13 -m venv venv
source venv/bin/activate
```

2. پکیج‌ها را نصب کنید:
```bash
pip install -r requirements.txt
```

3. MongoDB را اجرا کنید

4. فایل `.env` را تنظیم کنید

5. برنامه را اجرا کنید:
```bash
python manage.py runserver
# یا
uvicorn main:app --reload
```

## استفاده از manage.py

```bash
# اجرای سرور
python manage.py runserver

# باز کردن shell تعاملی
python manage.py shell
```

## API Documentation

بعد از اجرا، مستندات API در آدرس‌های زیر در دسترس است:

- Swagger UI: http://localhost:8585/docs
- ReDoc: http://localhost:8585/redoc

## Health Check

```bash
curl http://localhost:8585/api/v1/health
```
