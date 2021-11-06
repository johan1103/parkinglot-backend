#FROM python:3.9.5
#
#WORKDIR /home/
#
#RUN git clone https://github.com/johan1103/parkinglot-backend.git
#
#WORKDIR /home/parkinglot-backend/
#
#RUN pip install -r requirements.txt
#
#RUN pip install gunicorn
#
#RUN pip install mysqlclient
#
#RUN echo "SECRET_KEY=django-insecure-q$6x)3@^prkv%790e==^@*e_%@%v%ljj&o6zx2&-b)ni7p8y&(" > .env
#
#RUN python manage.py collectstatic
#
#EXPOSE 8000
#
#CMD ["bash", "-c", "python manage.py migrate --settings=smac.settings.deploy && gunicorn smac.wsgi --env DJANGO_SETTINGS_MODULE=smac.settings.deploy --bind 0.0.0.0:8000"]

FROM python:3.9.5

WORKDIR /home/

RUN git clone https://github.com/johan1103/parkinglot-backend.git

WORKDIR /home/parkinglot-backend/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-q$6x)3@^prkv%790e==^@*e_%@%v%ljj&o6zx2&-b)ni7p8y&(" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]




