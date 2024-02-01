FROM alpine:latest 

RUN apk --update add python3 

COPY . /usr/src/app

CMD "python3", "/usr/src/app/Multiplication.py"