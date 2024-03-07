FROM python:3.8-slim
RUN pip install DateTime
COPY buyer.py buyer.py
COPY sales.db sales.db
COPY tickets.txt tickets.txt
CMD ["python", "buyer.py"]