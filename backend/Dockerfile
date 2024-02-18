FROM python:slim-bullseye


RUN mkdir /backend
WORKDIR /backend
ADD . /backend
RUN pip install virtualenv
RUN virtualenv backend_env


RUN . backend_env/bin/activate
RUN apt-get update && apt-get install -y tesseract-ocr-all
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "app:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "8080"]