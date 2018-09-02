FROM ubuntu:latest

RUN apt-get install --reinstall -y locales

RUN sed -i 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen

RUN locale-gen pt_BR.UTF-8

ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR
ENV LC_ALL pt_BR.UTF-8

RUN dpkg-reconfigure --frontend noninteractive locales

ADD requirements.txt requirements.txt

ADD crontab /etc/cron.d/issue-cron

ADD create_issue.py /root/create_issue.py

ADD issue_body.md /root/issue_body.md

ADD env.json /root/env.json

ADD secret.json /root/secret.json

RUN apt-get update && apt-get -y install \
  cron \
  python3 \
  python3-pip

RUN pip3 install -r requirements.txt

RUN chmod 0644 /etc/cron.d/issue-cron

RUN crontab /etc/cron.d/issue-cron

RUN touch /var/log/cron_create.log && touch /var/log/cron_close.log

CMD ["cron", "-f"]
