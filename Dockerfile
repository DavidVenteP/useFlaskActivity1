FROM python:3.6

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY app/app.py /app
ADD app/static/ /app/static
ADD app/templates /app/templates
CMD python app.py