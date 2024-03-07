FROM debian
RUN apt-get update && apt-get install -y python3
ADD users.py /users.py
CMD ["/usr/bin/python3","/users.py"]