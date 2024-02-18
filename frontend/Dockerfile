FROM python:slim-bullseye


RUN mkdir /frontend
WORKDIR /frontend
ADD . /frontend
RUN pip install virtualenv
RUN virtualenv model_env
RUN . model_env/bin/activate
RUN pip install -r requirements.txt
RUN groupadd -r user && useradd -r -g user user
EXPOSE 8077
USER user

CMD ["uvicorn", "main:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "8077"]