FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 9999
CMD ["python", "app.py"]
