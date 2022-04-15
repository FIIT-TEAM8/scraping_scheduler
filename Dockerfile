FROM python:3.9-alpine

WORKDIR /scripts

COPY . /scripts

RUN pip install -r requirements.txt

RUN apk update && apk add tzdata

ENV TZ=Europe/Bratislava

COPY root /var/spool/cron/crontabs/root

CMD [ "/usr/sbin/crond", "-f", "-d8" ]