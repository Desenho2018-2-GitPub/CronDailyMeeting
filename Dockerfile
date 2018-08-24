FROM ubuntu:latest

RUN apt-get update && apt-get -y install cron

ADD crontab /etc/cron.d/hello-cron

RUN chmod 0644 /etc/cron.d/hello-cron

RUN crontab /etc/cron.d/hello-cron

RUN touch /var/log/cron.log

CMD ["cron", "-f"]