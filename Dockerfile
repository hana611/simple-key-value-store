# از یک image سبک Python استفاده می‌کنیم
FROM python:3.10-slim

# پوشه کاری داخل کانتینر
WORKDIR /app

# کپی فایل requirements و نصب وابستگی‌ها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# کپی فایل app.py
COPY app.py .

# پورت 5000 روی کانتینر
EXPOSE 5000

# دستور اجرا
CMD ["python", "app.py"]
