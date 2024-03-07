FROM debian
RUN apt-get update && apt-get install -y ncat
CMD ncat -l 2000 -k --exec /bin/cat