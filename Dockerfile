FROM python:3
RUN pip install django==3.2


COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py makemigrations --noinput
RUN python manage.py migrate --run-syncdb
RUN python manage.py collectstatic --noinput


# CMD ["python","manage.py","runserver","0.0.0.0:8001"]
CMD ["gunicorn", "--bind", "0.0.0.0:8001", "todo.wsgi"]
