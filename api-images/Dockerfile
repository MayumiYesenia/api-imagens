FROM python:3-slim
WORKDIR /programas/api-images
RUN apt-get update && apt-get install -y default-libmysqlclient-dev
RUN pip install flask mysql-connector-python
COPY . .
CMD [ "python", "./app.py" ]
