FROM python:3.11.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install gunicorn
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app

                               ## app : app
## module name(file name i.e. app.py) : flask object(app = flask(__name__))


