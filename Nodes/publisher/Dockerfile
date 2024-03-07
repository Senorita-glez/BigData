FROM python:3.8-slim
WORKDIR /app
COPY publish.py script.py
RUN pip install pika==1.2.0
CMD ["python",”-u”,"script.py"]