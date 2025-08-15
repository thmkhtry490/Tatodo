FROM python:3.13-slim

WORKDIR /app

# Install python packages
COPY requirments.txt .
RUN python -m pip install --no-cache-dir -r requirments.txt

COPY . .

# collect static for better load css in production mode
RUN python manage.py collectstatic --noinput

# Migrate sqlite database
RUN python manage.py migrate

CMD ["gunicorn", "mytodolist.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]